from aiogram import Bot, Dispatcher
from app.handlears import router
from dotenv import load_dotenv

import os
import logging
import asyncio 

load_dotenv()

API_TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)


async def main():
    if not API_TOKEN:
        logging.error("API_TOKEN is not set. Please check your .env file.")
        return
    try:
        bot = Bot(token=API_TOKEN)
        dp = Dispatcher()
        dp.include_router(router)
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Failed to start bot: {e}")
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stopped!')
        