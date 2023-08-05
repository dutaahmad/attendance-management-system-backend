from fastapi import APIRouter, status, Body, Depends
# from google.cloud.firestore_v1.document import DocumentReference;

from ...config.database import db

from .employee_model import Employee, EmployeeRequestBody
from .employee_service import add_employee, get_employee, update_employee, get_employee_profile

from ...config.auth_config import get_current_active_user

employee_router = APIRouter(prefix="/employee")


@employee_router.post(path="/", status_code=status.HTTP_201_CREATED)
def employee_create(payload: EmployeeRequestBody = Body(),
                    response: dict = Depends(get_current_active_user)) -> dict:

    res_id = add_employee(requestBody=payload)
    response = {
        "message": f"employee with id {res_id} has been created",
        "status_code": status.HTTP_201_CREATED
    }
    return response


@employee_router.get(path="/", status_code=status.HTTP_200_OK)
def employee_list(response: dict = Depends(get_current_active_user)) -> dict:
    response = {
        "data": get_employee(),
        "message": "get list of employee success",
        "status_code": status.HTTP_200_OK
    }
    return response


@employee_router.get(path="/{employee_id}", status_code=status.HTTP_200_OK)
def employee_by_id(employee_id: str,
                   response: dict = Depends(get_current_active_user)) -> dict:
    response = {
        "data": get_employee(employee_id=employee_id),
        "message": "get list of employee success",
        "status_code": status.HTTP_200_OK
    }
    return response


@employee_router.patch(path="/{employee_id}", status_code=status.HTTP_202_ACCEPTED)
def edit_employee(employee_id: str,
                  payload: EmployeeRequestBody = Body(),
                  response: dict = Depends(get_current_active_user)) -> dict:
    response = {
        "data": update_employee(employee_id=employee_id, payload=payload),
        "message": "update person success",
        "status_code": status.HTTP_202_ACCEPTED
    }
    return response


@employee_router.get(path="/profile/{employee_id}", status_code=status.HTTP_200_OK)
def employee_profile(employee_id: str,
                     response: dict = Depends(get_current_active_user)) -> dict:
    response = {
        "data": get_employee_profile(employee_id=employee_id),
        "message": "get employee profile success",
        "status_code": status.HTTP_200_OK
    }
    return response
