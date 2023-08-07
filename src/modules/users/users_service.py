from fastapi import status, HTTPException
from ...config.database import db

from .users_model import User, UserRequestBody
from ..attendance.attendance_model import Attendance
from ...config.auth_config import token_decoding


def get_logged_user_data(payload: Attendance):
    user_data = token_decoding(to_be_decoded=payload.access_token)

    return user_data


def add_user(requestBody: UserRequestBody):
    if (not requestBody.username) or (requestBody.username == ""):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Field required!!!"
        )

    if (not requestBody.password) or (requestBody.password == ""):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Field required!!!"
        )

    newUser = {
        "username": requestBody.username,
        "password": requestBody.password,
        "is_employee": True if requestBody.employee_id == True else False,
        "employee_id": requestBody.employee_id if requestBody.employee_id else "",
        "is_active": True,
    }

    updateTime, userRef = db.collection("user").add(newUser)

    return userRef.id
