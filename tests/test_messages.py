#!/usr/bin/env -S uv run
from os import environ

from boto3 import client
from faker import Faker

import wapy

eum = client('socialmessaging')
faker = Faker(locale='es_MX')
phone_number = environ['PHONE_NUMBER']
phone_number_id = environ['PHONE_NUMBER_ID']


def test_text_message():
    message = wapy.models.messages.TextMessage(
        to=phone_number,
        text=wapy.models.messages.Text(
            body='Saludos',
        ),
        type=wapy.constants.MessageType.TEXT,
    )
    eum.send_whatsapp_message(
        message=message.dump(),
        metaApiVersion='v23.0',
        originationPhoneNumberId=phone_number_id,
    )


def test_template_message():
    message = wapy.models.messages.TemplateMessage(
        to=phone_number,
        type=wapy.constants.MessageType.TEMPLATE,
        template=wapy.models.messages.Template(
            name='delivery_canceled_out_of_stock',
            language=wapy.models.messages.Language(
                code='es_MX',
            ),
            components=[
                wapy.models.messages.BodyComponent(
                    type=wapy.constants.ComponentType.BODY,
                    parameters=[
                        wapy.models.messages.TextParameter(
                            type=wapy.constants.ParameterType.TEXT,
                            text=faker.numerify('######'),
                            parameter_name='delivery_number',
                        ),
                    ],
                ),
                wapy.models.messages.URLButtonComponent(
                    type=wapy.constants.ComponentType.BUTTON,
                    index=0,
                    sub_type=wapy.constants.ComponentSubType.URL,
                    parameters=[
                        wapy.models.messages.URLButtonParameter(
                            text=faker.uuid4(),
                            type=wapy.constants.ButtonParameterType.TEXT,
                        )
                    ],
                ),
            ],
        ),
    )
    eum.send_whatsapp_message(
        message=message.dump(),
        metaApiVersion='v23.0',
        originationPhoneNumberId=phone_number_id,
    )
