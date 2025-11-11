from pydantic import BaseModel


class Media(BaseModel):
    id: str
    """
    The media object ID.
    """

    """
    https://www.postman.com/meta/whatsapp-business-platform/documentation/wlk6lh4/whatsapp-cloud-api?entity=folder-18dd8543-9314-4e2c-9f86-4c5fab8fa4e1#fa59d67b-dc6f-446a-a0fd-f97537afbd2e
    """

    caption: str | None = None
    """
    Describes the specified image, document, or video. Do not use it with audio or sticker media.
    """

    filename: str | None = None
    """
    Describes the filename for the specific document. Use only with document media.
    """
