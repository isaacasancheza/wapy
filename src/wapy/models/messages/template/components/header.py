from typing import Literal

from pydantic import BaseModel

from wapy import constants
from wapy.models.messages.template.parameters import Parameter


class HeaderComponent(BaseModel):
    type: Literal[constants.ComponentType.HEADER]
    """
    Describes the component type. 
    
    For text-based templates, only body is supported.
    """

    parameters: list[Parameter] | None = None
    """
    The namespace of the template.
    """
