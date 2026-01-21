from datetime import datetime, timedelta, timezone

MAX_ATTEMPTS = 5
BLOCK_WINDOW = timedelta(minutes=10)

_attempts = {}  # storage em memória


def register_failed_attempt(key: str) -> int:
    now = datetime.now(timezone.utc)

    data = _attempts.get(key)

    if not data:
        _attempts[key] = {
            "count": 1,
            "last_attempt": now
        }
        return 1

    # reseta se passou o tempo
    if now - data["last_attempt"] > BLOCK_WINDOW:
        _attempts[key] = {
            "count": 1,
            "last_attempt": now
        }
        return 1

    data["count"] += 1
    data["last_attempt"] = now
    return data["count"]


def is_blocked(key: str) -> bool:
    data = _attempts.get(key)

    if not data:
        return False

    if data["count"] >= MAX_ATTEMPTS:
        if datetime.now(timezone.utc) - data["last_attempt"] <= BLOCK_WINDOW:
            return True

    return False