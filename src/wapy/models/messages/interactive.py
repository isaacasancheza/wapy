from typing import Literal

from wapy import constants
from wapy.models.messages.message import Message
from wapy.models.messages.objects.interactive import Interactive


class InteractiveMessage(Message):
    type: Literal[constants.MessageType.INTERACTIVE]
    """
    The type of message you want to send. 
    """

    interactive: Interactive
    """
    **Added to Webhook if type is `interactive`.**
    
    When a customer has interacted with your message, an interactive object is included in the `Messages` object.
    """
