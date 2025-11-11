from typing import Annotated

from pydantic import Field

from .button import (
    QuickReplyButtonParameter,
    URLButtonParameter,
)
from .currency import (
    CurrencyParameter,
)
from .date_time import (
    DateTimeParameter,
)
from .document import (
    DocumentParameter,
)
from .image import (
    ImageParameter,
)
from .text import (
    TextParameter,
)

type Parameter = Annotated[
    TextParameter
    | ImageParameter
    | CurrencyParameter
    | DateTimeParameter
    | DocumentParameter,
    Field(
        discriminator='type',
    ),
]
"""
For text-based templates, the only supported parameter types are `text`, `currency`, and `date_time`.
"""
