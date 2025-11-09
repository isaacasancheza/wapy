from typing import Literal

from pydantic import BaseModel

from wapy import constants


class URLButtonParameter(BaseModel):
    type: Literal[constants.ButtonParameterType.TEXT]
    """
    Specifies the type of parameter for the button.
    """

    text: str
    """
    Developer-provided suffix that is appended to the predefined prefix URL in the template.
    """


class QuickReplyButtonParameter(BaseModel):
    type: Literal[constants.ButtonParameterType.PAYLOAD]
    """
    Specifies the type of parameter for the button.
    """

    payload: str
    """
    Developer-defined payload that is returned when the button is clicked in addition to the display text on the button.
    """
