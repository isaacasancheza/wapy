from typing import Annotated

from pydantic import Field

from .body import (
    BodyComponent,
)
from .button import (
    QuickReplyButtonComponent,
    URLButtonComponent,
)
from .header import (
    HeaderComponent,
)

type ButtonComponent = Annotated[
    URLButtonComponent | QuickReplyButtonComponent,
    Field(
        discriminator='sub_type',
    ),
]

type Component = Annotated[
    BodyComponent | ButtonComponent | HeaderComponent,
    Field(
        discriminator='type',
    ),
]
