from typing import Literal

from wapy import constants
from wapy.models.messages.objects.media import Video
from wapy.models.messages.objects.message import Message


class VideoMessage(Message):
    type: Literal[constants.MessageType.VIDEO]
    """
    The type of message you want to send. 
    """

    video: Video
    """
    A media object containing a video.
    """
