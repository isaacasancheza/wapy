from pydantic import BaseModel

from wapy import constants


class ContactAddress(BaseModel):
    type: constants.ContactAddressType | None = None
    """
    Address type.
    """

    street: str | None = None
    """
    Steet number and name.
    """

    city: str | None = None
    """
    The name of the city.
    """

    state: str | None = None
    """
    The abbreviation name of the state.
    """

    zip: str | None = None
    """
    The ZIP code.
    """

    country: str | None = None
    """
    The full name of the country.
    """

    country_code: str | None = None
    """
    The two-letter country abbreviation.
    """
