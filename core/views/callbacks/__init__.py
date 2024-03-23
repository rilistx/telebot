__all__ = [
    'callback_bot',
    ]


from aiogram import Router, F

from core.views.callbacks.products import product
from core.views.callbacks.data import ProductInfo


def callback_bot(router: Router) -> None:
    router.callback_query.register(product, ProductInfo.filter(F.action == 'create'))
