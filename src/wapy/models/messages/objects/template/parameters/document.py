from typing import Literal

from pydantic import BaseModel

from wapy import constants
from wapy.models.messages.objects.media import Media


class DocumentParameter(BaseModel):
    """
    https://www.postman.com/meta/whatsapp-business-platform/documentation/wlk6lh4/whatsapp-cloud-api?entity=folder-c0d42cc5-436e-490a-8f61-1c447da01c86#fa59d67b-dc6f-446a-a0fd-f97537afbd2e
    """

    type: Literal[constants.ParameterType.DOCUMENT]
    """
    Describes the parameter type. 
    """

    document: Media
    """
    A media object of type document. 
    
    Only PDF documents are supported for media-based message templates.
    """
