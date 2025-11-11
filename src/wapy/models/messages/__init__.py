from typing import Annotated

from pydantic import Field

from .objects import (
    Currency,
    DateTime,
    Media,
    Reaction,
    Template,
    Text,
)
from .objects.template import (
    BodyComponent,
    ButtonComponent,
    Component,
    CurrencyParameter,
    DateTimeParameter,
    DocumentParameter,
    HeaderComponent,
    ImageParameter,
    Language,
    Parameter,
    QuickReplyButtonComponent,
    QuickReplyButtonParameter,
    TextParameter,
    URLButtonComponent,
    URLButtonParameter,
)
from .template import (
    TemplateMessage,
)
from .text import (
    TextMessage,
)

type Message = Annotated[
    TextMessage | TemplateMessage,
    Field(
        discriminator='type',
    ),
]
