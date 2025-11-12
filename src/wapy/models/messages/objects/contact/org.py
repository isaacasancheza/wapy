from pydantic import BaseModel


class ContactOrg(BaseModel):
    title: str | None = None
    """
    The contact's business title.
    """

    company: str | None = None
    """
    Name of the contact's company.
    """

    department: str | None = None
    """
    Name of the contact's department.
    """
