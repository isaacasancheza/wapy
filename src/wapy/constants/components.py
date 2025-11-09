from enum import StrEnum


class ComponentType(StrEnum):
    BODY = 'body'
    BUTTON = 'button'
    HEADER = 'header'


class ComponentSubType(StrEnum):
    URL = 'url'
    QUICK_REPLY = 'quick_reply'
