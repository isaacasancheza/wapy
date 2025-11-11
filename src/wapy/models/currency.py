from pydantic import BaseModel


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
