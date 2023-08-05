from pydantic import BaseModel


class Coordinates(BaseModel):
    latitude: str
    longitude: str


class Attendance(BaseModel):
    # user_id: str
    # attend_time: str
    access_token: str
    coordinates: Coordinates
    distance: float
