from typing import Literal

from wapy import constants
from wapy.models.messages.message import Message
from wapy.models.messages.objects.media import Document


class DocumentMessage(Message):
    type: Literal[constants.MessageType.DOCUMENT]
    """
    The type of message you want to send. 
    """

    document: Document
    """
    A media object containing a document.
    """
