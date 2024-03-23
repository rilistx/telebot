__all__ = [
    'start_bot', 'stop_bot',
    'start_cmd_bot', 'echo_bot',
    ]


from aiogram import Router, F
from aiogram.filters import CommandStart

from .main import start, stop
from .views import start_cmd, echo, inline_handler


# Start bot
def start_bot(router: Router) -> None:
    router.startup.register(start)


# Stop bot
def stop_bot(router: Router) -> None:
    router.shutdown.register(stop)


def start_cmd_bot(router: Router) -> None:
    router.message.register(start_cmd, CommandStart())


def inline_handler_bot(router: Router) -> None:
    router.message.register(inline_handler, F.text == 'Посмотреть')


def echo_bot(router: Router) -> None:
    router.message.register(echo)
