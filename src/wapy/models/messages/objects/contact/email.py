from pydantic import BaseModel

from wapy import constants


class ContactEmail(BaseModel):
    type: constants.ContactEmailType | None = None
    """
    Email type.
    """

    email: str | None = None
    """
    Email address.
    """
