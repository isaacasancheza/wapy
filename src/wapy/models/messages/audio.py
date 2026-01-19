from typing import Literal

from wapy import constants
from wapy.models.messages.message import Message
from wapy.models.messages.objects.media import Audio


class AudioMessage(Message):
    type: Literal[constants.MessageType.AUDIO]
    """
    The type of message you want to send. 
    """

    audio: Audio
    """
    A media object containing audio.
    """
