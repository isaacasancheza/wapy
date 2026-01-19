from typing import Literal

from wapy import constants
from wapy.models.messages.message import Message
from wapy.models.messages.objects.contact import Contact


class ContactMessage(Message):
    type: Literal[constants.MessageType.CONTACTS]
    """
    The type of message you want to send. 
    """

    contact: Contact
    """
    A contacts object.
    """
