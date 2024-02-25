from aiogram import types

from core.callbacks.data import ProductInfo


async def product(callback: types.CallbackQuery, callback_data: ProductInfo):
    action = callback_data.action

    response = f"Вы хотите {action} продукт!"

    await callback.message.answer(response)
    await callback.answer()
