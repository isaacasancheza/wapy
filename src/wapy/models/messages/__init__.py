from typing import Annotated

from pydantic import Field

from .audio import (
    AudioMessage,
)
from .contact import (
    ContactMessage,
)
from .document import (
    DocumentMessage,
)
from .image import (
    ImageMessage,
)
from .location import (
    LocationMessage,
)
from .objects import (
    Audio,
    Contact,
    ContactAddress,
    ContactEmail,
    ContactName,
    ContactOrg,
    ContactPhone,
    ContactURL,
    Currency,
    DateTime,
    Document,
    Image,
    Location,
    MessageContext,
    Reaction,
    Sticker,
    Template,
    Text,
    Video,
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
from .reaction import (
    ReactionMessage,
)
from .sticker import (
    StickerMessage,
)
from .template import (
    TemplateMessage,
)
from .text import (
    TextMessage,
)
from .video import (
    VideoMessage,
)

type Message = Annotated[
    TextMessage
    | AudioMessage
    | ImageMessage
    | VideoMessage
    | ContactMessage
    | StickerMessage
    | DocumentMessage
    | LocationMessage
    | TemplateMessage,
    Field(
        discriminator='type',
    ),
]
