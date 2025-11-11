from pydantic import BaseModel

from wapy.models.messages.objects.template.components import Component
from wapy.models.messages.objects.template.language import Language


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
