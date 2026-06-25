from pydantic import BaseModel, computed_field, model_validator

from wapy import constants


class MessageContext(BaseModel):
    message_id: str


class Message(BaseModel):
    to: str | None = None
    recipient: str | None = None
    context: MessageContext | None = None

    @model_validator(mode='after')
    def validate_addressing(self) -> 'Message':
        if self.to is None and self.recipient is None:
            raise ValueError('one of to or recipient is required')
        if self.to is not None and self.recipient is not None:
            raise ValueError('to and recipient are mutually exclusive')
        return self

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
