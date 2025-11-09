from enum import IntEnum, StrEnum


class DayOfWeekName(StrEnum):
    MONDAY = 'MONDAY'
    TUESDAY = 'TUESDAY'
    WEDNESDAY = 'WEDNESDAY'
    THURSDAY = 'THURSDAY'
    FRIDAY = 'FRIDAY'
    SATURDAY = 'SATURDAY'
    SUNDAY = 'SUNDAY'


class DayofWeekNumber(IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


class CalendarType(StrEnum):
    GREGORIAN = 'GREGORIAN'
    SOLAR_HIJRI = 'SOLAR_HIJRI'
