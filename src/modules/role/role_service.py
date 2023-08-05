from fastapi import status, HTTPException
from ...config.database import db

from .role_model import Role

def get_role(role_id:str = None) -> list:

    if role_id == None:
        return_data = []
        roleRef = db.collection(u'role').where(u'is_active', u'==', True)
        docs = roleRef.stream()
        for doc in docs:
            data: dict = doc.to_dict()
            data['role_id'] = doc.id
            return_data.append(data)

    else:
        return_data = db.collection(u'role').document(role_id).get().to_dict()

    return return_data

def add_role(payload: Role):

    if (not payload.role_name) or (payload.role_name == ""):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Field required!!!"
        )
    
    newRole = {
        u'role_name': payload.role_name,
        u'is_active': True
    }

    updateTime, roleRef = db.collection(u'role').add(newRole)
    
    return roleRef.id

def update_role(role_id: str, payload: Role):

    roleRef = db.collection(u'role').document(
        role_id)

    if (not payload.role_name) or (payload.role_name == ""):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Field required!!!"
        )

    roleRef.update(
        {
            u'role_name': payload.role_name,
            u'is_active': True
        }
    )

    return (db.collection(u'role').document(
            role_id).get().to_dict())