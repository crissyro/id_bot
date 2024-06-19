from aiogram import Bot, Dispatcher, types, F
from dotenv import load_dotenv

import os
import logging
import asyncio 

API_TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

