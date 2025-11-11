from typing import Literal

from pydantic import BaseModel

from wapy import constants


class TextParameter(BaseModel):
    """
    https://www.postman.com/meta/whatsapp-business-platform/documentation/wlk6lh4/whatsapp-cloud-api?entity=folder-c0d42cc5-436e-490a-8f61-1c447da01c86#fa59d67b-dc6f-446a-a0fd-f97537afbd2e
    """

    type: Literal[constants.ParameterType.TEXT]
    """
    Describes the parameter type. 
    """

    text: str
    """
    The message of the text.
    
    For the `header component`, the character limit is 60 characters. 
    
    For the `body component`, the character limit is 1024.

    The exception to these character limits applies to template messages in the following conditions:

    - When sending a **`template`** message with a body component **`only`**, the character limit for the `text` parameter and the full template text is 32768 characters.
    - When sending a **`template`** message with **`body`** and other components, The character limit for the `text` parameter and the full template text is 1024 characters.
    """

    parameter_name: str | None = None
    """
    The parameter name.
    """
