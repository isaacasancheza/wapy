from typing import Annotated

from pydantic import Field

from .button import (
    QuickReplyButtonParameter,
    URLButtonParameter,
)
from .currency import (
    Currency,
    CurrencyParameter,
)
from .date_time import (
    DateTime,
    DateTimeParameter,
)
from .text import (
    TextParameter,
)

type Parameter = Annotated[
    TextParameter | CurrencyParameter | DateTimeParameter,
    Field(
        discriminator='type',
    ),
]
