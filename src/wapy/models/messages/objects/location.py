from pydantic import BaseModel


class Location(BaseModel):
    name: str | None = None
    """
    The name of the location.
    """

    address: str | None = None
    """
    The address of the location. This field is only displayed if **`name`** is present.
    """

    latitude: float
    """
    The latitude of the location.
    """

    longitude: float
    """
    The longitude of the location.
    """
