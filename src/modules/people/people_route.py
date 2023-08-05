from fastapi import APIRouter, status, Body, Depends

from ...config.database import db

from .people_model import Person
from .people_service import get_people, add_person, update_person

from ...config.auth_config import get_current_active_user

people_router = APIRouter(prefix="/people")


@people_router.post(path="/", status_code=status.HTTP_201_CREATED)
def person_create(payload: Person = Body(), 
                  response: dict = Depends(get_current_active_user)) -> dict:

    response = {
        "message": f"person with id {add_person(payload=payload)} has been created",
        # "created_time": update_time,
        "status_code": status.HTTP_201_CREATED
    }

    return response


@people_router.get(path="/", status_code=status.HTTP_200_OK)
def people_list(response: dict = Depends(get_current_active_user)) -> dict:

    data = get_people()

    response = {
        "data": sorted(data, key=(lambda dictionary: dictionary['fullname'])),
        "message": "get list of people success",
        "status_code": status.HTTP_200_OK
    }

    return response


@people_router.get(path="/{person_id}", status_code=status.HTTP_200_OK)
def person(person_id: str, response: dict = Depends(get_current_active_user)) -> dict:

    response = {
        "data": get_people(person_id=person_id),
        "message": "get person success",
        "status_code": status.HTTP_200_OK
    }
    return response


@people_router.patch(path="/{person_id}", status_code=status.HTTP_202_ACCEPTED)
def edit_person(person_id: str, 
                payload: Person = Body(), 
                response: dict = Depends(get_current_active_user)) -> dict:

    response = {
        "data": update_person(person_id=person_id, payload=payload),
        "message": "update person success",
        "status_code": status.HTTP_202_ACCEPTED
    }

    return response
