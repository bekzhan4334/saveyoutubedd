from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = '5697862008:AAE5VIeS4r5BIevj5hWk9OYhOUlx9ASdcM8'

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
