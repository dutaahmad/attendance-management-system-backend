from pydantic import BaseModel


class Person(BaseModel):
    fullname: str
    # password: str | None = None
    # is_active: bool | None = True;