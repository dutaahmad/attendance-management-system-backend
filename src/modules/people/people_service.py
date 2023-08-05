from fastapi import status, HTTPException
from ...config.database import db

from .people_model import Person


def get_people(person_id: str = None) -> list:

    if person_id == None:
        return_data = []
        peopleRef = db.collection(u'people').where(u'is_active', u'==', True)
        docs = peopleRef.stream()
        for doc in docs:
            data: dict = doc.to_dict()
            data['person_id'] = doc.id
            return_data.append(data)

    else:
        return_data = db.collection(u'people').document(
            person_id).get().to_dict()

    return return_data


def add_person(payload: Person):

    if (not payload.fullname) or (payload.fullname == ""):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Field required!!!"
        )

    newPerson = {
        u'fullname': payload.fullname,
        u'is_active': True
    }

    updateTime, personRef = db.collection(u'people').add(newPerson)

    return personRef.id


def update_person(person_id: str, payload: Person):

    peopleRef = db.collection(u'people').document(
        person_id)

    if (not payload.fullname) or (payload.fullname == ""):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Field required!!!"
        )

    peopleRef.update(
        {
            u'fullname': payload.fullname,
            u'is_active': True
        }
    )

    return (db.collection(u'people').document(
            person_id).get().to_dict())