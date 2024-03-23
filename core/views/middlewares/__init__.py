__all__ = [
    'session_bot', 'scheduler_bot',
    ]


from aiogram import Router

from core.database.engine import async_session
from core.scheduler.tasks import scheduler_tasks
from core.views.middlewares.database import DataBaseSession
from core.views.middlewares.scheduler import Scheduler


scheduler = scheduler_tasks()


def session_bot(router: Router) -> None:
    router.message.middleware.register(DataBaseSession(session_pool=async_session))


def scheduler_bot(router: Router) -> None:
    router.message.middleware.register(Scheduler(scheduler=scheduler))
