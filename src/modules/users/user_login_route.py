
from datetime import datetime, timedelta

import jwt
from jwt import PyJWTError

from fastapi import APIRouter, status, Body, HTTPException, Depends

# from ...main import SECRET_KEY, ALGORITHM;
from ...config.database import db
from ...config.auth_config import authDataStore, token_encoding, token_decoding, get_current_active_user

from .users_model import User

auth_router = APIRouter(prefix="/auth")


@auth_router.post(path="/login", status_code=status.HTTP_200_OK)
def user_login(payload: User = Body()) -> dict:

    userResults: list = db.collection(u'user').where(
        u'username', u'==', payload.username
    ).where(
        u'password', u'==', payload.password
    ).where(
        u'is_active', u'==', True
    ).get()

    users = [item.to_dict() for item in userResults]

    if (users.__len__()) != 1:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="user data you provide is invalid!!!"
        )

    to_be_encoded: dict = users[0]

    # authDataStore.add_data(to_be_encoded)

    access_token = token_encoding(
        to_be_encoded=to_be_encoded
    )

    to_be_stored = token_decoding(
        to_be_decoded=access_token
    )

    authDataStore.add_data(to_be_stored)

    return {
        "access_token": access_token,
        "status_code": status.HTTP_200_OK
    }


@auth_router.post(path="/get_current_user", status_code=status.HTTP_200_OK)
def get_current_user(
        payload: dict = Body(),
        response: dict = Depends(get_current_active_user)
    ) -> dict:

    # user_datas = authDataStore.get_datas()

    # print(user_datas)

    # user_data = jwt.decode(
    #     jwt=payload["access_token"],
    #     key=SECRET_KEY,
    #     algorithms=ALGORITHM
    # )

    try:
        user_data = token_decoding(
        to_be_decoded=payload["access_token"]
    )
    except PyJWTError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

    # print("is it true the user is logged in?", user_datas[0] == user_data)

    return {
        "data": user_data,
        "status_code": status.HTTP_200_OK,
        "message": "get current user success!",
        # "auth_singleton_datas": authDataStore.get_data()
    }
