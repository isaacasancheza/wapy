from typing import Literal

from pydantic import BaseModel

from wapy import constants
from wapy.models.messages.message import Message
from wapy.models.messages.template.components import Component


class Language(BaseModel):
    """
    https://www.postman.com/meta/whatsapp-business-platform/documentation/wlk6lh4/whatsapp-cloud-api?entity=folder-dc659eae-7847-432e-b09c-a079a0b4801e#fa59d67b-dc6f-446a-a0fd-f97537afbd2e
    """

    code: str
    """
    The code of the language or locale to use. This field accepts both language (for example, `en`) and language_locale (for example, `en_US`) formats. 
    """


class Template(BaseModel):
    """
    https://www.postman.com/meta/whatsapp-business-platform/documentation/wlk6lh4/whatsapp-cloud-api?entity=folder-a7a8962d-1e3f-43c8-8667-58458ac3b568#fa59d67b-dc6f-446a-a0fd-f97537afbd2e
    """

    name: str
    """
    The name of the template.
    """

    language: Language
    """
    Specifies a language object. Specifies the language the template may be rendered in.

    Only the **`deterministic`** language policy works with media template messages.
    """

    components: list[Component]
    """
     An array of components objects that contain the parameters of the message.
    """


class TemplateMessage(Message):
    type: Literal[constants.MessageType.TEMPLATE]
    """
    The type of message you want to send. 
    """

    template: Template
    """
    A template object.
    """
