from pydantic import BaseModel


class ContactName(BaseModel):
    """
    At least one of the optional parameters needs to be included along with the formatted_name parameter.
    """

    prefix: str | None = None
    """
    Name prefix.
    """

    suffix: str | None = None
    """
    Name suffix.
    """

    first_name: str | None = None
    """
    First name.
    """

    middle_name: str | None = None
    """
    Middle name.
    """

    last_name: str | None = None
    """
    Last name.
    """

    formatted_name: str
    """
    Full name, as it normally appears.
    """
