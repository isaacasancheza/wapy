"""
https://www.postman.com/meta/whatsapp-business-platform/documentation/wlk6lh4/whatsapp-cloud-api?entity=folder-18dd8543-9314-4e2c-9f86-4c5fab8fa4e1#fa59d67b-dc6f-446a-a0fd-f97537afbd2e
"""

from pydantic import BaseModel


class Audio(BaseModel):
    """
    A media object.
    """

    id: str
    """
    The media object ID.
    """


class Image(BaseModel):
    """
    A media object.
    """

    id: str
    """
    The media object ID.
    """

    caption: str | None = None
    """
    Describes the specified image.
    """


class Video(BaseModel):
    """
    A media object.
    """

    id: str
    """
    The media object ID.
    """

    caption: str | None = None
    """
    Describes the specified video.
    """


class Sticker(BaseModel):
    """
    A media object.
    """

    id: str
    """
    The media object ID.
    """


class Document(BaseModel):
    """
    A media object.
    """

    id: str
    """
    The media object ID.
    """

    filename: str | None = None
    """
    Describes the filename for the specific document.
    """
