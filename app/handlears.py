from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Hello, I can send telegram id')