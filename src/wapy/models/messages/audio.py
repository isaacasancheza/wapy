from typing import Literal

from wapy import constants
from wapy.models.messages.objects.media import Audio
from wapy.models.messages.objects.message import Message


class AudioMessage(Message):
    type: Literal[constants.MessageType.AUDIO]
    """
    The type of message you want to send. 
    """

    audio: Audio
    """
    A media object containing audio.
    """
