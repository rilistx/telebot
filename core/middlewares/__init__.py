__all__ = [
    'session_bot'
    ]


from aiogram import Router

from core.database.engine import async_session
from core.middlewares.database import DataBaseSession


# Start bot
def session_bot(router: Router) -> None:
    router.message.middleware.register(DataBaseSession(session_pool=async_session))
