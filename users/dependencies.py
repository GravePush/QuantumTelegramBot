import jwt
from fastapi import HTTPException, Request, Depends, Response
from jwt import InvalidTokenError, ExpiredSignatureError
from sqlalchemy.ext.asyncio import AsyncSession

from config import SECRET_KEY, ALGORITHM
from database import get_db
from users.service import UserService


def get_token(request: Request):
    token = request.cookies.get("api_access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Token not found!")
    return token


async def get_current_user(
        session: AsyncSession = Depends(get_db),
        token: str = Depends(get_token)

):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired!")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token!")
    user = await UserService.get_one_or_none(session=session, username=username)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found!")

    return user
