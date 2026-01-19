from typing import Literal

from wapy import constants
from wapy.models.messages.message import Message
from wapy.models.messages.objects.reaction import Reaction


class ReactionMessage(Message):
    type: Literal[constants.MessageType.REACTION]
    """
    The type of message you want to send. 
    """

    reaction: Reaction
    """
    A reaction object.
    """
