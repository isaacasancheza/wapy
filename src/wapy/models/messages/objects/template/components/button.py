from typing import Annotated, Literal

from pydantic import BaseModel, Field

from wapy import constants
from wapy.models.messages.objects.template.parameters import (
    QuickReplyButtonParameter,
    URLButtonParameter,
)


class URLButtonComponent(BaseModel):
    type: Literal[constants.ComponentType.BUTTON]
    """
    Describes the component type.
    """

    parameters: list[URLButtonParameter] = Field(min_length=1)
    """
    The namespace of the template.
    """

    sub_type: Literal[constants.ComponentSubType.URL]
    """
    The type of button to create.
    """

    index: Annotated[int, Field(ge=0, le=2)]
    """
    The position index of the button. You can have up to 3 buttons using index values of 0 to 2.
    """


class QuickReplyButtonComponent(BaseModel):
    type: Literal[constants.ComponentType.BUTTON]
    """
    Describes the component type.
    """

    parameters: list[QuickReplyButtonParameter] = Field(min_length=1)
    """
    The namespace of the template.
    """

    sub_type: Literal[constants.ComponentSubType.QUICK_REPLY]
    """
    The type of button to create. 
    """

    index: int = Field(ge=0, le=2)
    """
    The position index of the button. You can have up to 3 buttons using index values of 0 to 2.
    """


type ButtonComponent = Annotated[
    URLButtonComponent | QuickReplyButtonComponent,
    Field(
        discriminator='sub_type',
    ),
]
