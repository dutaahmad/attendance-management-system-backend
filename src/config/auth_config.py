from datetime import datetime, timedelta
import jwt
from jwt import PyJWTError

from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer


SECRET_KEY = "mY_JwT_s3CRe7_K3y"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="auth/login"
)


class AuthSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AuthSingleton, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance


class AuthDataStore(AuthSingleton):
    def __init__(self):
        self.data_dict = {}
        self.datas = list(self.data_dict)

    def add_data(self, new_data):
        self.datas.append(new_data)

    def get_datas(self) -> list:
        return self.datas

    def get_data(self, payload:dict):
        filtered_data = filter( (lambda filter_param: filter_param == payload ) , self.datas)
        return filtered_data

authDataStore = AuthDataStore()

def token_encoding(to_be_encoded: dict = {}) -> str:

    token_expire: datetime = (datetime.now() + timedelta(minutes=30))

    to_be_encoded.update(
        {
            "exp": token_expire
        }
    )

    access_token:str = jwt.encode(
        payload=to_be_encoded,
        key=SECRET_KEY,
        algorithm=ALGORITHM
    )

    return access_token

def token_decoding(to_be_decoded: str) -> dict:
    
    token_data: dict = jwt.decode(
        jwt=to_be_decoded,
        key=SECRET_KEY,
        algorithms=ALGORITHM
    )

    
    return token_data

async def get_current_user(token: str = Depends(oauth2_scheme)):

    authDataStore = AuthDataStore()

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        decoded_token_data = token_decoding(to_be_decoded=token)
        username: str = decoded_token_data.get("username")
        if username is None:
            raise credentials_exception
        # token_data = TokenData(username=username)
    except PyJWTError:
        raise credentials_exception
    user = authDataStore.get_data(payload=decoded_token_data)
    if user is None:
        raise credentials_exception

    return user

async def get_current_active_user(current_user = Depends(get_current_user)):
    
    if not authDataStore.get_data(current_user):

    # if current_user not in authDataStore.get_datas():
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user