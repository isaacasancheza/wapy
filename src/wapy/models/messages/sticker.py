from typing import Literal

from wapy import constants
from wapy.models.messages.message import Message
from wapy.models.messages.objects.media import Sticker


class StickerMessage(Message):
    type: Literal[constants.MessageType.STICKER]
    """
    The type of message you want to send. 
    """

    sticker: Sticker
    """
    A `media object` containing a sticker. 
    
    Currently, we only support third-party static stickers. Static stickers must be 512x512 pixels and cannot exceed 100 KB. 
    
    Animated stickers must be 512x512 pixels and cannot exceed 500 KB.
    """
