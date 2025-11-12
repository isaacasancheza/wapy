from typing import Literal

from wapy import constants
from wapy.models.messages.objects.contact import Contact
from wapy.models.messages.objects.message import Message


class ContactMessage(Message):
    type: Literal[constants.MessageType.CONTACTS]
    """
    The type of message you want to send. 
    """

    contact: Contact
    """
    A contacts object.
    """
