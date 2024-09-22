#! /bin/python3

import asyncio, logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN


bot= Bot(TOKEN)
dp=Dispatcher()



@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello!')

@dp.message(Command('help'))
async def cmd_help(message:Message):
    await message.answer('This is command /help .')


@dp.message(F.text=='/next')
async def cmd_help(message:Message):
    await message.answer('This is command /next .')

@dp.message(F.photo)
async def cmd_photo(message: Message):
    await message.answer(f'Id photo:{message.photo[-1].file_id}')


@dp.message(Command('get_photo'))
async def cmd_get_photo(message:Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMSZu_4KM49pxAeHHjNiZaZ3_iHoowAAkLpMRugAnlLfbertm7TuTwBAAMCAANtAAM2BA',caption='Any photo.')

async def main():
    await dp.start_polling(bot)

if __name__=='__main__':
        logging.basicConfig(level=logging.INFO)
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            print('Exit')