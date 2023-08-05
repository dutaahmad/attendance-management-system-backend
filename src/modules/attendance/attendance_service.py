from datetime import datetime

from ...config.database import db
from .attendance_model import Attendance
from ...config.auth_config import token_decoding


def record_attendance(payload: Attendance) -> dict:

    user_data = token_decoding(
        payload.access_token
    )

    userResults: list = db.collection(u'user').where(
        u'username', u'==', user_data["username"]
    ).where(
        u'password', u'==', user_data["password"]
    ).where(
        u'is_active', u'==', True
    ).stream()

    users = []
    for item in userResults:
        data: dict = item.to_dict()
        data["user_id"] = item.id
        users.append(data)

    newAttendance = {
        u'user_id': users[0]["user_id"],
        u'attend_time': str(datetime.now()),
        u'attend_coordinates_latitude': payload.coordinates.latitude,
        u'attend_coordinates_longitude': payload.coordinates.longitude,
        u'distance': payload.distance,
    }

    updateTime, attendanceRef = db.collection(
        u'attendances').add(newAttendance)

    return attendanceRef.id
