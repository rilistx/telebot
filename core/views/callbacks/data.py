from aiogram.filters.callback_data import CallbackData


class ProductInfo(CallbackData, prefix='product'):
    action: str
