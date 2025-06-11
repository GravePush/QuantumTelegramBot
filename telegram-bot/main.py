import asyncio

import httpx
from aiogram import Bot, Dispatcher, F

from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

from config import BOT_API, API_URL

bot = Bot(token=BOT_API)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Напиши /posts чтобы посмотреть посты.")


@dp.message(Command("posts"))
async def posts_handler(message: Message):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{API_URL}/posts")
            response.raise_for_status()
        except httpx.HTTPError as e:
            await message.answer(f"Ошибка при получении постов. {e}")
            return

    posts = response.json()
    if not posts:
        await message.answer("Постов нет.")
        return

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=post["headline"], callback_data=str(post["id"]))]
            for post in posts
        ]
    )

    await message.answer("Выберите пост:", reply_markup=keyboard)


@dp.callback_query(F.data)
async def callback_handler(callback: CallbackQuery):
    callback_data = callback.data

    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    if callback_data == "back_to_posts":
        await posts_handler(callback.message)
        await callback.answer()
        return

    async with httpx.AsyncClient() as client:
        try:
            post_id = int(callback_data)
            response = await client.get(f"{API_URL}/posts/{post_id}")
            response.raise_for_status()
        except httpx.HTTPError:
            await callback.message.edit_text("Ошибка при получении поста.")
            return

    post = response.json()

    text = (
        f"Заголовок - {post['headline']}\n"
        f"Описание - {post['text']}\n"
        f"Дата создания - {post['created_at']}"
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="back_to_posts")]
        ]
    )

    await bot.send_message(chat_id=callback.message.chat.id, text=text, reply_markup=keyboard)
    await callback.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
