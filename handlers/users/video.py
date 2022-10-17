from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from loader import dp,bot
from states import Dowload

from pytube import YouTube
import os
import uuid

def dowload_video(url, type='audio'):
    yt = YouTube(url)
    audio_id = uuid.uuid4().fields[-1]
    if type == 'audio':
        yt.streams.filter(only_audio=True).first().download("audio", f"{audio_id}.mp3")
        return f"{audio_id}.mp3"
    elif type == 'video':
        return f"{audio_id}.mp4"


@dp.message_handler(Command('audio'))
async def start_dow(message: types.Message):
    await message.answer(text=f"Hi, {message.from_user.full_name}, send me the link to the video and I will reply to you with audio type")
    await Dowload.dowload.set()


@dp.message_handler(state=Dowload.dowload)
async def dowload(message: types.Message, state: FSMContext):
    title = dowload_video(message.text)
    audio = open(f'audio/{title}', 'rb')
    await message.answer(text="Downloaded, sending the audio")
    try:
        await bot.send_audio(message.chat.id, audio)
        await bot.send_message(message.chat.id, text='')
    except:
        await message.answer(text='File is too big')
    os.remove(f'audio/{title}')
    await state.finish()




