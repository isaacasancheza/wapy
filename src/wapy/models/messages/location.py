from typing import Literal

from wapy import constants
from wapy.models.messages.objects.location import Location
from wapy.models.messages.objects.message import Message


class LocationMessage(Message):
    type: Literal[constants.MessageType.LOCATION]
    """
    The type of message you want to send. 
    """

    location: Location
    """
    A location object.
    """
