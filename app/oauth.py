from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "02fd0gfr0g3d1g32g0f20fg31gf1g32dfsg01sag1g"
ALGORITHM = "HS256"
ACESS_TOKEN_EXPIRE_MINUTES = 60

def create_acess_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt