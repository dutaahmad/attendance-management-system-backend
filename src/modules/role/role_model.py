from pydantic import BaseModel


class Role(BaseModel):
    role_name: str
    # password: str | None = None
    # is_active: bool | None = True;