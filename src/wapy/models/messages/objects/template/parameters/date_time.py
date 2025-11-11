from typing import Literal

from pydantic import BaseModel

from wapy import constants
from wapy.models.messages.objects.date_time import DateTime


class DateTimeParameter(BaseModel):
    """
    https://www.postman.com/meta/whatsapp-business-platform/documentation/wlk6lh4/whatsapp-cloud-api?entity=folder-c0d42cc5-436e-490a-8f61-1c447da01c86#fa59d67b-dc6f-446a-a0fd-f97537afbd2e
    """

    type: Literal[constants.ParameterType.DATE_TIME]
    """
    Describes the parameter type. 
    """

    date_time: DateTime
    """
    A date_time object.
    """

    parameter_name: str | None = None
    """
    The parameter name.
    """
