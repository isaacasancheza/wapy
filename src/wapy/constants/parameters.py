from enum import StrEnum


class ParameterType(StrEnum):
    TEXT = 'text'
    IMAGE = 'image'
    CURRENCY = 'currency'
    DOCUMENT = 'document'
    DATE_TIME = 'date_time'
