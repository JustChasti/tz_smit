from loguru import logger
import functools


def default_decorator(errormessage: str):
    def iternal_decorator(function):
        def wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except Exception as e:
                logger.exception(e)
                return {'info': errormessage}
        return wrapper
    return iternal_decorator


def async_decorator(errormessage: str):
    def iternal_decorator(function):
        @functools.wraps(function)
        async def wrapper(*args, **kwargs):
            try:
                return await function(*args, **kwargs)
            except Exception as e:
                logger.exception(e)
                return {'info': errormessage}
        return wrapper
    return iternal_decorator
