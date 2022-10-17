from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Start the bot"),
            types.BotCommand("help", "Help"),
            types.BotCommand("audio", "Convert yt video to audio")
        ]
    )