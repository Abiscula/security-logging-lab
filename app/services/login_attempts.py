import redis

MAX_ATTEMPTS = 5
BLOCK_WINDOW_SECONDS = 60  # 1 minuto

redis_client = redis.Redis(host="redis", port=6379, decode_responses=True)

def _key(key: str) -> str:
    return f"login_attempts:{key}"


# Registra uma tentativa de login com falha para a chave informada.
def register_failed_attempt(key: str) -> int:
    redis_key = _key(key)

    count = redis_client.incr(redis_key)

    # define o TTL apenas na primeira tentativa
    if count == 1:
        redis_client.expire(redis_key, BLOCK_WINDOW_SECONDS)

    return count



# Verifica se a chave informada está bloqueada por excesso de tentativas.
def is_blocked(key: str) -> bool:
    redis_key = _key(key)

    count = redis_client.get(redis_key)

    if not count:
        return False

    return int(count) >= MAX_ATTEMPTS