from enum import Enum


class LogType(str, Enum):
    EVENT = "EVENT"
    REQUEST = "REQUEST"
