from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder

main=ReplyKeyboardMarkup(keyboard=
                         [
                             [KeyboardButton(text='1')],
                             [KeyboardButton(text='2'),KeyboardButton(text='3')]
                             ],resize_keyboard=True)


settings=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='github',url='https://github.com/andriy-klmts/Telegram-bot')]])


async def keybord_buttonbuilder():
    keybrd=ReplyKeyboardBuilder()
    for tmp in ['bmw','nisan','pego']:
        keybrd.add(KeyboardButton(text=tmp))
    return keybrd.adjust(2).as_markup()