from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import os

from .modules.users.users_route import user_router
from .modules.users.user_login_route import auth_router
from .modules.attendance.attendance_route import attendance_router
from .modules.people.people_route import people_router
from .modules.role.role_route import role_router
from .modules.employee.employee_route import employee_router

SECRET_KEY = "mY_JwT_s3CRe7_K3y"
ALGORITHM = "HS256"

app = FastAPI()

origins = [
    "http://localhost:5000",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:5173",
    "http://149.51.37.178:3000",
    "http://149.51.37.178:3001",
    "https://attendance-management-system-frontend-skripsi-wildan.vercel.app",
    "https://attendance-management-system-frontend-dp4l01bo2-skripsi-wildan.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(attendance_router)
app.include_router(auth_router)
app.include_router(people_router)
app.include_router(role_router)
app.include_router(employee_router)


@app.get("/")
async def root():
    resp = {"message": """ This is Wildan's Skripsi API """}

    return resp


def run_app(app_name: str):
    uvicorn.run(
        app=app_name,
        host="0.0.0.0",
        port=(int(os.getenv("PORT", default=5555))),
        workers=5,
        log_level="debug",
        reload=True,
    )
