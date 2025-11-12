from pydantic import BaseModel

from wapy import constants


class ContactPhone(BaseModel):
    type: constants.ContactPhoneType | None = None
    """
    Phone type.
    """

    wa_id: str | None = None
    """
    WhatsApp ID.
    """

    phone: str | None = None
    """
    Automatically populated with the wa_id value as a formatted phone number.
    """
