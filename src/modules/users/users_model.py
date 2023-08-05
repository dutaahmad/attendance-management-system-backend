from pydantic import BaseModel
import jwt


class User(BaseModel):
    username: str
    password: str | None = None
    # is_active: bool | None = True;

class UserRequestBody(BaseModel):
    username: str
    password: str
    employee_id: str