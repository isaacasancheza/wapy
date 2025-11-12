from pydantic import BaseModel, computed_field

from wapy import constants


class MessageContext(BaseModel):
    message_id: str


class Message(BaseModel):
    to: str
    context: MessageContext | None = None

    @computed_field
    def recipient_type(self) -> constants.RecipientType:
        """
        Messaging service used for the request.
        """
        return constants.RecipientType.INDIVIDUAL

    @computed_field
    def messaging_product(self) -> constants.MessagingProduct:
        """
        Currently, you can only send messages to individuals. Set this value to `individual`.
        """
        return constants.MessagingProduct.WHATSAPP

    def dump(self) -> str:
        return self.model_dump_json(
            exclude_none=True,
        )
