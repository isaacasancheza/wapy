from pydantic import BaseModel

from wapy import constants


class ContactURL(BaseModel):
    url: str | None = None
    """
    The URL.
    """

    type: constants.ContactURLType | None = None
    """
    URL type.
    """
