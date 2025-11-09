from typing import Annotated

from pydantic import Field

from . import (
    template,
    text,
)
from .message import (
    Context,
)

type Message = Annotated[
    text.TextMessage | template.TemplateMessage,
    Field(
        discriminator='type',
    ),
]
