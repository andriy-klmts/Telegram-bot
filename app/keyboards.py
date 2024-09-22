from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder


main = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Button 1", callback_data="one"),
        InlineKeyboardButton(text="Button 2", callback_data="two")
    ],
    [
        InlineKeyboardButton(text="Button 3", callback_data="three")
    ]
])


settings=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='github',url='https://github.com/andriy-klmts/Telegram-bot')]])


async def keybord_buttonbuilder():
    keybrd=InlineKeyboardBuilder()
    for tmp in ['bmw','nisan','pego']:
        keybrd.add(InlineKeyboardButton(text=tmp,url='https://www.youtube.com/watch?v=QvENfMFhP60&list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM&index=5'))
    return keybrd.adjust(2).as_markup()