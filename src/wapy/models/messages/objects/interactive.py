from pydantic import BaseModel

from wapy import constants


class InteractiveButtonReply(BaseModel):
    """
    https://www.postman.com/meta/whatsapp-business-platform/documentation/wlk6lh4/whatsapp-cloud-api?entity=folder-a2322035-934e-43aa-aa97-a640b58468d1&sideView=agentMode#fa59d67b-dc6f-446a-a0fd-f97537afbd2e
    """

    id: str
    """
    The unique identifier of the button.
    """

    title: str
    """
    The title of the button.
    """


class InteractiveListReply(BaseModel):
    """
    https://www.postman.com/meta/whatsapp-business-platform/documentation/wlk6lh4/whatsapp-cloud-api?entity=folder-90043148-d3be-4cc2-a94f-201efbe6baf7&sideView=agentMode#fa59d67b-dc6f-446a-a0fd-f97537afbd2e
    """

    id: str
    """
    The unique identifier (ID) of the selected row.
    """

    title: str
    """
    The title of the selected row.
    """

    description: str
    """
    The description of the selected row.
    """


class Interactive(BaseModel):
    """
    https://www.postman.com/meta/whatsapp-business-platform/documentation/wlk6lh4/whatsapp-cloud-api?entity=folder-3636f9e0-41d8-43d3-ac5e-1df7d68072b8&sideView=agentMode#fa59d67b-dc6f-446a-a0fd-f97537afbd2e
    """

    type: constants.InteractiveType
    """
    Contains the type of interactive object. Supported options are:
    """

    button_reply: InteractiveButtonReply | None = None
    """
    **Used on Webhooks related to Reply Buttons.**
    
    Contains a button reply object.
    """

    list_reply: InteractiveListReply | None = None
    """
    **Used on Webhooks related to List Messages**
    
    Contains a list reply object.
    """
