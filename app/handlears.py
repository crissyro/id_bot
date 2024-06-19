from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()

user_data = {}

@router.message(CommandStart())
async def kb(message: Message):
    username = message.from_user.username
    user_id = message.from_user.id
    user_data[username] = user_id
    await message.answer(f'@{username}, ваш Telegram ID: {user_id}')
    await message.answer(f'Больше у меня никакого функционала нет )')    

@router.message(F.text)
async def text(message: Message):
    await message.answer(f'Не спамь!')
    
