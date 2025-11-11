from pydantic import BaseModel


class Reaction(BaseModel):
    """
    https://www.postman.com/meta/whatsapp-business-platform/documentation/wlk6lh4/whatsapp-cloud-api?entity=folder-dbb99b87-b24b-4d5d-9da6-8e860f6cbbd4
    """

    emoji: str
    """
    The emoji used for the reaction.

    All emojis are supported, however only one emoji can be sent in a reaction message. Set this value to "" (empty string) to remove the reaction. 
    
    Unicode is not supported. However, unicode values can be Java or JavaScript-escape encoded.
    """

    message_id: str
    """
    Specifies the WhatsApp message ID (WAMID) that this reaction is being sent to. 

     You cannot send a reaction to a **`message_id`** that previously sent or received reaction messages.
    """
