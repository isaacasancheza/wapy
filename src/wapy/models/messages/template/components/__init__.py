from typing import Annotated

from pydantic import Field

from .body import (
    BodyComponent,
)
from .button import (
    ButtonComponent,
    QuickReplyButtonComponent,
    URLButtonComponent,
)
from .header import (
    HeaderComponent,
)

type Component = Annotated[
    BodyComponent | ButtonComponent | HeaderComponent,
    Field(
        discriminator='type',
    ),
]
