from fastapi import APIRouter, status, Body, Depends

from ...config.database import db

from .role_model import Role
from .role_service import add_role, get_role, update_role

from ...config.auth_config import get_current_active_user

role_router = APIRouter(prefix="/role")

@role_router.post(path="/", status_code=status.HTTP_201_CREATED)
def role_create(payload: Role = Body(),
                response: dict = Depends(get_current_active_user)) -> dict:

    response = {
        "message": f"role with id {add_role(payload=payload)} has been created",
        # "created_time": update_time,
        "status_code": status.HTTP_201_CREATED
    }

    return response

@role_router.get(path="/", status_code=status.HTTP_200_OK)
def role_list(response: dict = Depends(get_current_active_user)) -> dict:

    response = {
        "data": get_role(),
        "message": "get list of roles success",
        "status_code": status.HTTP_200_OK
    }

    return response

@role_router.get(path="/{role_id}", status_code=status.HTTP_200_OK)
def role(role_id:str,
        response: dict = Depends(get_current_active_user)) -> dict:

    response = {
        "data": get_role(role_id=role_id),
        "message": "get role success",
        "status_code": status.HTTP_200_OK
    }

    return response

@role_router.patch(path="/{role_id}", status_code=status.HTTP_202_ACCEPTED)
def edit_role(role_id: str, 
            payload: Role = Body(), 
            response: dict = Depends(get_current_active_user)) -> dict:
    response = {
        "data": update_role(role_id=role_id, payload=payload),
        "message": "update person success",
        "status_code": status.HTTP_202_ACCEPTED
    }
    return response