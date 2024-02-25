from aiogram.utils.keyboard import InlineKeyboardBuilder

from core.callbacks.data import ProductInfo


def inline_builder_keyboard():
    inline_builder = InlineKeyboardBuilder()
    inline_builder.button(text='Добавить', callback_data=ProductInfo(action='create'))
    inline_builder.button(text='Посмотреть', callback_data=ProductInfo(action='read'))
    inline_builder.button(text='Изменить', callback_data=ProductInfo(action='update'))
    inline_builder.button(text='Удалить', callback_data=ProductInfo(action='delete'))

    inline_builder.adjust(2, 1, 1)
    return inline_builder.as_markup()
