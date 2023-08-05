from fastapi import APIRouter, status, Body, HTTPException, Depends

# import google
from google.cloud.firestore_v1.document import DocumentReference;

from ...config.database import db;
from ...config.auth_config import get_current_active_user

from .attendance_model import Attendance
from .attendance_service import record_attendance

attendance_router = APIRouter(prefix="/attendance")

@attendance_router.get(path="/", status_code=status.HTTP_200_OK)
def attendance_list() -> dict:

    docs = db.collection(u'attendances').stream()

    attendanceList = []
    for item in docs:
        data:dict = item.to_dict()
        for key, value in data.items():
            if type(value) == DocumentReference:
                data[key] = value.id
                        
        attendanceList.append(data)


    return {
        "data": attendanceList,
        "message": "get list of attendances success",
        "status_code": status.HTTP_200_OK
    }

@attendance_router.post(path="/", status_code=status.HTTP_201_CREATED)
def record_attendance_user(payload: Attendance = Body(), response: dict = Depends(get_current_active_user)):
    # record_attendance(payload)
    response = {
        # "data": record_attendance(payload),
        "message": f"Attendance Recorded with the id of {record_attendance(payload)}",
        "status": status.HTTP_201_CREATED
    }
    return response

@attendance_router.get(path="/test", status_code=status.HTTP_200_OK)
def protected_endpoint(
    response: str = Depends(get_current_active_user)
) ->list:
    

    response = "this is a sample data which only a logged user can see"
    
    return {
        "data": response,
        "message": "get list of attendances success",
        "status_code": status.HTTP_200_OK
    }