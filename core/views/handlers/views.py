from aiogram import types

from sqlalchemy.ext.asyncio import AsyncSession

from core.database.models import User
from core.database.orm import queryset
from core.keyboards.inline.products import inline_builder_keyboard


async def start_cmd(message: types.Message) -> None:
    await message.answer("Это команда старт")


async def inline_handler(message: types.Message) -> None:
    await message.answer("Выбери необходимое действие: ", reply_markup=inline_builder_keyboard())


async def echo(message: types.Message, session: AsyncSession) -> None:
    query = User(username='rilistx', age=26)
    await queryset.create_data(session, query)
    await message.answer(message.text)
