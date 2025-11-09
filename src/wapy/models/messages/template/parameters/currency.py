from typing import Literal

from pydantic import BaseModel

from wapy import constants


class Currency(BaseModel):
    """
    https://www.postman.com/meta/whatsapp-business-platform/documentation/wlk6lh4/whatsapp-cloud-api?entity=folder-a50fe825-3880-4cab-8860-5f3795c76695#fa59d67b-dc6f-446a-a0fd-f97537afbd2e
    """

    code: str
    """
    The currency code as defined in [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217#Active_codes).
    """

    amount_1000: int
    """
    The amount multiplied by 1000.
    """

    fallback_value: str
    """
    The default text if localization fails.
    """


class CurrencyParameter(BaseModel):
    """
    https://www.postman.com/meta/whatsapp-business-platform/documentation/wlk6lh4/whatsapp-cloud-api?entity=folder-c0d42cc5-436e-490a-8f61-1c447da01c86#fa59d67b-dc6f-446a-a0fd-f97537afbd2e
    """

    type: Literal[constants.ParameterType.CURRENCY]
    """
    Describes the parameter type. 

    For text-based templates, the only supported parameter types are `text`, `currency`, and `date_time`.
    """

    currency: Currency
    """
    A currency object.
    """
