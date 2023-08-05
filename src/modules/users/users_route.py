from fastapi import APIRouter, status, Body, HTTPException, Depends

from ...config.database import db
from ...config.auth_config import get_current_active_user

from .users_model import User, UserRequestBody
from .users_service import add_user

user_router = APIRouter(prefix="/users")


@user_router.get(path="/", status_code=status.HTTP_200_OK)
def user_list() -> dict:

    usersRef = db.collection(u'user')
    docs = usersRef.stream()

    # userList = [ item.to_dict() for item in docs ]
    userList = []
    for doc in docs:
        data: dict = doc.to_dict()
        data['user_id'] = doc.id
        data.pop('password')
        userList.append(data)

    return {
        "data": userList,
        "message": "get list of users success",
        "status_code": status.HTTP_200_OK
    }


@user_router.post(path="/", status_code=status.HTTP_201_CREATED)
def create_user(
    payload: UserRequestBody = Body(),
    response: dict = Depends(get_current_active_user)
) -> dict:

    data = add_user(requestBody=payload)

    return {
        "message": f"user with id {data} has been created",
        "status_code": status.HTTP_201_CREATED
    }


# def create_user(payload: dict = Body()) -> dict:

#     expectedPayload = ['username', 'password'];

#     if list(payload.keys()) != expectedPayload:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User Body is invalid!!!");

#     newUser = {
#         u'username': payload['username'],
#         u'password': payload['password'],
#         u'is_active': True
#     };

#     update_time, userRef = db.collection(u'users').add(newUser);

#     return {
#         "message": f"user with id {userRef.id} has been created",
#         "created_time": update_time,
#         "status_code": status.HTTP_201_CREATED
#     };
