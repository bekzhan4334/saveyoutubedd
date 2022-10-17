from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp

@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("List of command: ",
            "/start - Start dialog",
            "/help -  Get help",
            "/audio - Download the video and get audio")
    await message.answer("\n".join(text))