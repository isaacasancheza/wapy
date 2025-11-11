from pydantic import BaseModel

from wapy import constants


class DateTime(BaseModel):
    """
    https://www.postman.com/meta/whatsapp-business-platform/documentation/wlk6lh4/whatsapp-cloud-api?entity=folder-71406858-f35e-4317-b5f0-77292f5b0c9f#fa59d67b-dc6f-446a-a0fd-f97537afbd2e
    """

    fallback_value: str
    """
    The default text if localization fails.
    """

    day_of_week: constants.DayOfWeekName | constants.DayofWeekNumber | None = None
    """
    If it is different from the value derived from the date (if specified), use the derived value. Both strings and numbers are accepted.
    """

    year: int | None = None
    """
    Specifies the year.
    """

    month: int | None = None
    """
    Specifies the month.
    """

    day_of_month: int | None = None
    """
    Specifies the day of the month.
    """

    hour: int | None = None
    """
    Specifies the hour.
    """

    minute: int | None = None
    """
    Specifies the minute.
    """

    calendar: constants.CalendarType | None = None
    """
    The type of calendar.
    """
