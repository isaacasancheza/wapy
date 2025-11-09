from enum import StrEnum


class MessageType(StrEnum):
    TEXT = 'text'
    TEMPLATE = 'template'
    DOCUMENT = 'document'
    IMAGE = 'image'
    INTERACTIVE = 'interactive'
    AUDIO = 'audio'
    CONTACTS = 'contacts'
    LOCATION = 'location'
    STICKER = 'sticker'
    VIDEO = 'video'


class RecipientType(StrEnum):
    INDIVIDUAL = 'individual'


class MessagingProduct(StrEnum):
    WHATSAPP = 'whatsapp'
