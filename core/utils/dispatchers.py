from core import middlewares
from core import handlers
from core import callbacks


# Middlewares
def middleware_dispatchers(dispatcher):
    middleware_list = [
        middlewares.session_bot(dispatcher),
    ]

    return [middleware for middleware in middleware_list]


# Handlers
def handler_dispatchers(dispatcher):
    handler_list = [
        handlers.start_bot(dispatcher),
        handlers.stop_bot(dispatcher),
        handlers.start_cmd_bot(dispatcher),
        handlers.inline_handler_bot(dispatcher),
        handlers.echo_bot(dispatcher),
    ]

    return [handler for handler in handler_list]


# Callbacks
def callback_dispatchers(dispatcher):
    callback_list = [
        callbacks.callback_bot(dispatcher),
    ]

    return [callback for callback in callback_list]


# All Dispatcher (Middlewares & Handlers)
def all_dispatchers(dispatcher):
    return middleware_dispatchers(dispatcher), handler_dispatchers(dispatcher), callback_dispatchers(dispatcher)
