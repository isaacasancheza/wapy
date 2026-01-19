from typing import Literal

from wapy import constants
from wapy.models.messages.message import Message
from wapy.models.messages.objects.template.template import Template


class TemplateMessage(Message):
    type: Literal[constants.MessageType.TEMPLATE]
    """
    The type of message you want to send. 
    """

    template: Template
    """
    A template object.
    """
