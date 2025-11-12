from typing import Literal

from wapy import constants
from wapy.models.messages.objects.media import Image
from wapy.models.messages.objects.message import Message


class ImageMessage(Message):
    type: Literal[constants.MessageType.IMAGE]
    """
    The type of message you want to send. 
    """

    image: Image
    """
    A media object containing an image.
    """
