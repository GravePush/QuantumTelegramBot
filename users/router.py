from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession

from config import ACCESS_TOKEN_EXPIRE_MINUTES
from database import get_db
from users import UserModel
from users.auth import get_password_hash, authenticate_user, create_access_token
from users.dependencies import get_current_user
from users.schemas import UserIn, UserResponseMessage, UserSchema, UserOut
from users.service import UserService

users_router = APIRouter(prefix="/users", tags=["Users"])


@users_router.post("/register", response_model=UserResponseMessage)
async def register_user(user: UserIn, db: AsyncSession = Depends(get_db)):
    existing_user = await UserService.get_one_or_none(session=db, username=user.username)
    if existing_user:
        raise HTTPException(status_code=401, detail="User already exist!")
    hashed_password = get_password_hash(password=user.password)
    await UserService.create(
        session=db,
        username=user.username,
        password=hashed_password
    )
    return UserResponseMessage(
        message=f"{user.username} successful registered!"
    )


@users_router.post("/login", response_model=UserResponseMessage)
async def login(
        user: UserIn,
        response: Response,
        db: AsyncSession = Depends(get_db)
):
    auth_user = await authenticate_user(
        username=user.username,
        password=user.password,
        session=db
    )

    if not auth_user:
        raise HTTPException(status_code=401, detail="Invalid username or password!")

    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token_expires_to_seconds = int(ACCESS_TOKEN_EXPIRE_MINUTES) * 60

    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )
    response.set_cookie("api_access_token", access_token, httponly=True, max_age=access_token_expires_to_seconds)
    return UserResponseMessage(
        message=f"{user.username} successful logged!"
    )


@users_router.post("/me", response_model=UserOut)
async def get_me(user: UserModel = Depends(get_current_user)):
    return user


@users_router.post("/logout", response_model=UserResponseMessage)
async def logout(response: Response, user: UserModel = Depends(get_current_user)):
    response.delete_cookie("api_access_token")
    return UserResponseMessage(message=f"{user.username} logout.")
