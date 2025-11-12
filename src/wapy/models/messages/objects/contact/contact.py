from datetime import date

from pydantic import BaseModel

from .address import ContactAddress
from .email import ContactEmail
from .name import ContactName
from .org import ContactOrg
from .phone import ContactPhone
from .url import ContactURL


class Contact(BaseModel):
    name: ContactName
    """
    Specifies the name object. 
    """

    org: ContactOrg | None = None
    """
    Specifies the org object.
    """

    urls: list[ContactURL] | None = None
    """
    Specifies an array of url objects.
    """

    emails: list[ContactEmail] | None = None
    """
    Specifies an array of email objects.
    """

    phones: list[ContactPhone] | None = None
    """
    Specifies an array of phone objects.
    """

    birthday: date | None = None
    """
    A YYYY-MM-DD formatted string.
    """

    addresses: list[ContactAddress] | None = None
    """
    Specifies an array of address objects.
    """
