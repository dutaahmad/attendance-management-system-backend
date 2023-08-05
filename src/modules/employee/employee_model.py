from pydantic import BaseModel
from ..people.people_model import Person
from ..role.role_model import Role


class Employee(BaseModel):
    person: Person
    role: Role
    # is_active: bool | None = True;


class EmployeeRequestBody(BaseModel):
    person_id: str
    role_id: str
    is_active: bool | None = True
