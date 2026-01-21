from datetime import datetime, timedelta, timezone
from typing import Dict

# Número máximo de tentativas permitidas dentro da janela de bloqueio
MAX_ATTEMPTS = 5

# Janela de tempo em que o bloqueio é aplicado após excesso de tentativas
BLOCK_WINDOW = timedelta(minutes=1)

# Armazena tentativas de login em memória
# key -> { count: int, last_attempt: datetime }
_attempts: Dict[str, dict] = {}


# Registra uma tentativa de login com falha para a chave informada.
# Retorna o número atual de tentativas.
def register_failed_attempt(key: str) -> int:
    now = datetime.now(timezone.utc)
    data = _attempts.get(key)

    # Primeira tentativa registrada
    if not data:
        _attempts[key] = {
            "count": 1,
            "last_attempt": now
        }
        return 1

    # Se a janela de bloqueio expirou, reinicia o contador
    if now - data["last_attempt"] > BLOCK_WINDOW:
        _attempts[key] = {
            "count": 1,
            "last_attempt": now
        }
        return 1

    # Incrementa tentativa dentro da janela
    data["count"] += 1
    data["last_attempt"] = now
    return data["count"]


# Verifica se a chave informada está bloqueada por excesso de tentativas.
def is_blocked(key: str) -> bool:
    data = _attempts.get(key)

    if not data:
        return False

    attempts_exceeded = data["count"] >= MAX_ATTEMPTS
    within_block_window = (
        datetime.now(timezone.utc) - data["last_attempt"] <= BLOCK_WINDOW
    )

    return attempts_exceeded and within_block_window