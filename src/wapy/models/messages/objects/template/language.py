from pydantic import BaseModel


class Language(BaseModel):
    """
    https://www.postman.com/meta/whatsapp-business-platform/documentation/wlk6lh4/whatsapp-cloud-api?entity=folder-dc659eae-7847-432e-b09c-a079a0b4801e#fa59d67b-dc6f-446a-a0fd-f97537afbd2e
    """

    code: str
    """
    The code of the language or locale to use. This field accepts both language (for example, `en`) and language_locale (for example, `en_US`) formats. 
    """
