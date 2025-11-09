from typing import Annotated, Literal

from pydantic import BaseModel, StringConstraints

from wapy import constants
from wapy.models.messages.message import Message


class Text(BaseModel):
    """
    https://www.postman.com/meta/whatsapp-business-platform/documentation/wlk6lh4/whatsapp-cloud-api?entity=folder-ab68266a-e8b7-4ff6-be23-ca665ee2576c#fa59d67b-dc6f-446a-a0fd-f97537afbd2e
    """

    body: Annotated[
        str,
        StringConstraints(
            max_length=4096,
        ),
    ]
    """
    The text of the text message that can contain URLs and supports formatting. To view available formatting options, see Text Object Formatting Options. 

    If you include URLs in your text **and** want to include a preview box in text messages (`"preview_url": true`), ensure it starts with `http://` or `https://`. You must include a hostname, since IP addresses are not matched.
    """

    preview_url: bool = False
    """
    By default, WhatsApp recognizes URLs and makes them clickable, but you can also include a preview box with more information about the link. Set this field to `true` if you want to include a URL preview box.

    The majority of the time when you send a URL, whether with a preview or not, the receiver of the message will see a URL that they can click on.

    URL previews are only rendered after one of the following has occurred:
    - The business has sent a message template to the user.
    - The user initiates a conversation with a "click to chat" link.
    - The user adds the business phone number to their address book and initiates a conversation.
    """


class TextMessage(Message):
    type: Literal[constants.MessageType.TEXT]
    text: Text
