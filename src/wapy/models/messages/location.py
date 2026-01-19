from typing import Literal

from wapy import constants
from wapy.models.messages.message import Message
from wapy.models.messages.objects.location import Location


class LocationMessage(Message):
    type: Literal[constants.MessageType.LOCATION]
    """
    The type of message you want to send. 
    """

    location: Location
    """
    A location object.
    """
