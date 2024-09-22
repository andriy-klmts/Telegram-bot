#! /bin/python3

import asyncio, logging

from aiogram import Bot, Dispatcher
from config import TOKEN
from app.handlers import rt

bot= Bot(TOKEN)
dp=Dispatcher()

async def main():
    dp.include_router(rt)
    await dp.start_polling(bot)

if __name__=='__main__':
        logging.basicConfig(level=logging.INFO)
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            print('Exit')