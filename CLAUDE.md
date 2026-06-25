# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
uv run --no-sync ruff format src tests   # format
uv run --no-sync ruff check src tests    # lint
uv run --no-sync mypy src                # type-check
uv run --no-sync pytest tests/           # run tests (requires env vars below)
```

Tests are integration tests that send real WhatsApp messages via AWS. They require:
- `PHONE_NUMBER` — recipient phone number
- `PHONE_NUMBER_ID` — WhatsApp origination phone number ID
- AWS credentials with `socialmessaging` access

## Architecture

The package exposes two top-level namespaces:

- `wapy.constants` — all enums (`MessageType`, `ComponentType`, `ComponentSubType`, `ParameterType`, `ButtonParameterType`, etc.)
- `wapy.models.messages` — all Pydantic models for building messages

`Message` (in `models/messages/message.py`) is the base class. It adds `to`, optional `context`, and computed fields `recipient_type` and `messaging_product`. Its `dump()` method returns `model_dump_json(exclude_none=True)` — the string passed directly to the AWS API.

Concrete message classes (`TextMessage`, `AudioMessage`, `ImageMessage`, `VideoMessage`, `DocumentMessage`, `StickerMessage`, `LocationMessage`, `ContactMessage`, `ReactionMessage`, `TemplateMessage`) each add a `type` literal field and a typed payload field.

`TemplateMessage` composes `Template → [Component] → [Parameter]`. Components and parameters are nested under `models/messages/objects/template/`.

Four names in `wapy.models.messages` are `type` aliases (discriminated unions), **not** instantiable classes:

| Alias | Discriminator | Concrete classes |
|---|---|---|
| `Message` | `type` | all concrete message classes |
| `Component` | `type` | `BodyComponent`, `HeaderComponent`, `ButtonComponent` |
| `ButtonComponent` | `sub_type` | `URLButtonComponent`, `QuickReplyButtonComponent` |
| `Parameter` | `type` | `TextParameter`, `ImageParameter`, `CurrencyParameter`, `DateTimeParameter`, `DocumentParameter` |

## Enum constants, not string literals

All discriminator fields (`type`, `sub_type`) require the actual `wapy.constants` enum values.
Pylance rejects plain strings even when the value matches.

```python
import wapy.constants

TemplateMessage(type=wapy.constants.MessageType.TEMPLATE, ...)
BodyComponent(type=wapy.constants.ComponentType.BODY, ...)
URLButtonComponent(
    type=wapy.constants.ComponentType.BUTTON,
    sub_type=wapy.constants.ComponentSubType.URL,
    index=0,          # int (0–2), not str
    ...
)
TextParameter(type=wapy.constants.ParameterType.TEXT, ...)
URLButtonParameter(type=wapy.constants.ButtonParameterType.TEXT, ...)
```

## List invariance

`list[TextParameter]` is not assignable to `list[Parameter]` (list is invariant).
Annotate intermediate variables when Pylance complains:

```python
params: list[wapy.models.messages.Parameter] = [TextParameter(...)]
components: list[wapy.models.messages.Component] = [BodyComponent(...), URLButtonComponent(...)]
```

## Full TemplateMessage example

```python
import wapy
import wapy.constants

message = wapy.models.messages.TemplateMessage(
    to=phone_number,
    type=wapy.constants.MessageType.TEMPLATE,
    template=wapy.models.messages.Template(
        name='your_template_name',
        language=wapy.models.messages.Language(code='en_US'),
        components=[
            wapy.models.messages.BodyComponent(
                type=wapy.constants.ComponentType.BODY,
                parameters=[
                    wapy.models.messages.TextParameter(
                        type=wapy.constants.ParameterType.TEXT,
                        text='123456',
                    ),
                ],
            ),
            wapy.models.messages.URLButtonComponent(
                type=wapy.constants.ComponentType.BUTTON,
                sub_type=wapy.constants.ComponentSubType.URL,
                index=0,
                parameters=[
                    wapy.models.messages.URLButtonParameter(
                        type=wapy.constants.ButtonParameterType.TEXT,
                        text='123456',
                    ),
                ],
            ),
        ],
    ),
)
```
