import redis
import os

class LoginAttemptService:

    def __init__(self, max_attempts=5, block_window=60):
        redis_host = os.getenv("REDIS_HOST")

        if not redis_host:
            raise RuntimeError("REDIS_HOST não definido")

        self.redis_client = redis.Redis(
            host=redis_host,
            port=6379,
            decode_responses=True
        )

        self.max_attempts = max_attempts
        self.block_window = block_window

    def _key(self, key: str) -> str:
        return f"login_attempts:{key}"

    # Registra uma tentativa de login com falha
    def register_failed_attempt(self, key: str) -> int:
        redis_key = self._key(key)

        count = self.redis_client.incr(redis_key)

        # define TTL só na primeira tentativa
        if count == 1:
            self.redis_client.expire(redis_key, self.block_window)

        return count

    # Verifica se a chave informada está bloqueada por excesso de tentativas.
    def is_blocked(self, key: str) -> bool:
        redis_key = self._key(key)

        count = self.redis_client.get(redis_key)

        if not count:
            return False

        return int(count) >= self.max_attempts