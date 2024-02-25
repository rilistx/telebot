from aiogram import Bot, Dispatcher

from core.database.engine import create_db, drop_db
from core.utils.environments import envs


async def start(bot: Bot) -> None:
    # await drop_db()
    await create_db()
    await bot.send_message(envs['admin_id'], text='Run bot 👍🏻')


async def stop(bot: Bot, dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await drop_db()
    await bot.send_message(envs['admin_id'], text='Stop bot 👎🏻')
