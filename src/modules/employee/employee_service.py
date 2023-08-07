from fastapi import status, HTTPException
from google.cloud.firestore_v1.document import DocumentReference

from ...config.database import db

from .employee_model import EmployeeRequestBody

from ..people.people_service import get_people
from ..people.people_model import Person

from ..role.role_service import get_role
from ..role.role_model import Role


def get_employee(employee_id: str = None) -> list:
    if employee_id == None:
        return_data = []
        employeeRef = db.collection("employee").where("is_active", "==", True)
        docs = employeeRef.stream()
        for item in docs:
            data: dict = item.to_dict()
            data["employee_id"] = item.id
            data["people"] = get_people(data["people"])
            data["role"] = get_role(data["role"])
            # if data["employee_motto"]:
            #     data.pop("employee_motto")
            return_data.append(data)
    else:
        return_data = db.collection("employee").document(employee_id).get().to_dict()
        return_data["people_data"] = get_people(return_data["people"])
        return_data["role_data"] = get_role(return_data["role"])

    print(return_data)

    return return_data


def get_employee_profile(employee_id: str = None) -> dict:
    return_data = db.collection("employee").document(employee_id).get().to_dict()
    return_data["people_data"] = get_people(return_data["people"])
    return_data["role_data"] = get_role(return_data["role"])
    return return_data


def add_employee(requestBody: EmployeeRequestBody):
    if (not requestBody.person_id) or (requestBody.person_id == ""):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Field required!!!"
        )

    if (not requestBody.role_id) or (requestBody.role_id == ""):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Field required!!!"
        )

    newEmployee = {
        "people": requestBody.person_id,
        "role": requestBody.role_id,
        "is_active": True,
    }

    updateTime, employeeRef = db.collection("employee").add(newEmployee)

    return employeeRef.id


def update_employee(employee_id: str, payload: EmployeeRequestBody):
    employeeRef = db.collection("employee").document(employee_id)

    if (not payload.person_id) or (payload.person_id == ""):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Field required!!!"
        )
    if (not payload.role_id) or (payload.role_id == ""):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Field required!!!"
        )

    employeeRef.update(
        {"people": payload.person_id, "role": payload.role_id, "is_active": True}
    )

    return db.collection("employee").document(employee_id).get().to_dict()
