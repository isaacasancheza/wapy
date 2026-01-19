from typing import Literal

from wapy import constants
from wapy.models.messages.message import Message
from wapy.models.messages.objects.text import Text


class TextMessage(Message):
    type: Literal[constants.MessageType.TEXT]
    """
    The type of message you want to send. 
    """

    text: Text
    """
    A text object.
    """
