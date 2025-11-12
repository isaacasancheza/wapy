from typing import Literal

from pydantic import BaseModel

from wapy import constants
from wapy.models.messages.objects.media import Image


class ImageParameter(BaseModel):
    """
    https://www.postman.com/meta/whatsapp-business-platform/documentation/wlk6lh4/whatsapp-cloud-api?entity=folder-c0d42cc5-436e-490a-8f61-1c447da01c86#fa59d67b-dc6f-446a-a0fd-f97537afbd2e
    """

    type: Literal[constants.ParameterType.IMAGE]
    """
    Describes the parameter type. 
    """

    image: Image
    """
    A media object of type image.
    """
