from enum import StrEnum


class ContactAddressType(StrEnum):
    HOME = 'HOME'
    WORK = 'WORK'


class ContactEmailType(StrEnum):
    HOME = 'HOME'
    WORK = 'WORK'


class ContactPhoneType(StrEnum):
    CELL = 'CELL'
    MAIN = 'MAIN'
    HOME = 'HOME'
    WORK = 'WORK'
    IPHONE = 'IPHONE'


class ContactURLType(StrEnum):
    HOME = 'HOME'
    WORK = 'WORK'
