from aiogram import  F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message,CallbackQuery
import app.keyboards as kb
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

rt=Router()

class Reg(StatesGroup):
    name=State()
    number=State()

@rt.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply('Hello!',reply_markup= kb.main)

@rt.message(Command('help'))
async def cmd_help(message:Message):
    await message.answer('This is command /help .')


@rt.message(F.text=='/next')
async def cmd_help(message:Message):
    await message.answer('This is command /next .')

@rt.message(F.photo)
async def cmd_photo(message: Message):
    await message.answer(f'Id photo:{message.photo[-1].file_id}')


@rt.message(Command('get_photo'))
async def cmd_get_photo(message:Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMSZu_4KM49pxAeHHjNiZaZ3_iHoowAAkLpMRugAnlLfbertm7TuTwBAAMCAANtAAM2BA',caption='Any photo.')

@rt.callback_query(F.data=='one')
async def one(callback:CallbackQuery):
    await callback.answer('')
    # await callback.message.answer('Hello one.',reply_markup=await kb.keybord_buttonbuilder())
    await callback.message.edit_text('Hello one.',reply_markup=await kb.keybord_buttonbuilder())


@rt.message(Command('reg'))
async def reg_one(message:Message,state:FSMContext):
    await state.set_state(Reg.name)
    await message.answer(f'Input name:{await state.get_data()}')

@rt.message(Reg.name)
async def reg_two(message: Message, state:FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Input number')


@rt.message(Reg.number)
async def reg_three(message: Message, state:FSMContext):
    await state.update_data(number=message.text)
    data=await state.get_data()
    await message.answer(f' Thank! {data}')
    await state.clear()
