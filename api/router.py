from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas import PostSchema, PostIn, PostUpdate, PostOutMessage
from database import get_db
from api.service import PostService
from users import UserModel
from users.dependencies import get_current_user

posts_router = APIRouter(prefix="/posts", tags=["Posts"])


@posts_router.get("", response_model=List[PostSchema])
async def get_posts(
        db: AsyncSession = Depends(get_db)
):
    posts = await PostService.get_all(session=db)
    if not posts:
        raise HTTPException(status_code=404, detail="Posts not found!")
    return posts


@posts_router.get("/my", response_model=List[PostSchema])
async def get_my_posts(
        db: AsyncSession = Depends(get_db),
        user: UserModel = Depends(get_current_user)
):
    posts = await PostService.get_all(session=db, user_id=user.id)
    if not posts:
        raise HTTPException(status_code=404, detail="Posts not found!")
    return posts


@posts_router.get("/{post_id}", response_model=PostSchema)
async def get_post_by_id(post_id: int, db: AsyncSession = Depends(get_db)):
    post = await PostService.get_one_by_id(session=db, item_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found!")
    return post


@posts_router.post("", response_model=PostOutMessage)
async def create_post(
        post: PostIn,
        user: UserModel = Depends(get_current_user),
        db: AsyncSession = Depends(get_db)
):
    await PostService.create(
        session=db,
        headline=post.headline,
        text=post.text,
        user_id=user.id
    )
    return PostOutMessage(
        message=f"{post.headline} was created!"
    )


@posts_router.patch("", response_model=PostOutMessage)
async def update_post(
        post_id: int,
        post_schema: PostUpdate,
        user: UserModel = Depends(get_current_user),
        db: AsyncSession = Depends(get_db)
):
    post = await PostService.get_one_by_id(session=db, item_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found!")

    if user.id != post.user_id:
        raise HTTPException(status_code=403, detail="You don't have permission to edit this post!")

    update_data = post_schema.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update!")

    await PostService.update(
        session=db,
        item_id=post_id,
        **update_data
    )
    return PostOutMessage(
        message=f"{post.headline} was updated!"
    )


@posts_router.delete("", response_model=PostOutMessage)
async def delete_post(
        post_id: int,
        user: UserModel = Depends(get_current_user),
        db: AsyncSession = Depends(get_db)
):
    post = await PostService.get_one_by_id(session=db, item_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found!")

    if user.id != post.user_id:
        raise HTTPException(status_code=403, detail="You don't have permission to delete this post!")

    await PostService.delete(session=db, item_id=post_id)
    return PostOutMessage(
        message=f"{post.headline} was deleted!"
    )
