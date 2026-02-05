from enum import Enum


class LoginErrors(str, Enum):
    INVALID_CREDENTIALS = "INVALID_CREDENTIALS"  # usuário ou senha inválidos
    USER_NOT_FOUND = "USER_NOT_FOUND"  # usuário inexistente
    USER_BLOCKED = "USER_BLOCKED"  # conta bloqueada
    ACCOUNT_DISABLED = "ACCOUNT_DISABLED"  # conta desativada
    TOO_MANY_ATTEMPTS = "TOO_MANY_ATTEMPTS"  # brute force / rate limit
