from loguru import logger
from functools import wraps


def log_decorator(func):
    """
    A decorator that logs the function name and arguments before execution,
    and the return value after execution.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Executing function: {func.__name__}")
        logger.info(f"Arguments: {args}")
        logger.info(f"Keyword arguments: {kwargs}")

        try:
            # Call the original function
            result = func(*args, **kwargs)
            logger.info(f"Function {func.__name__} returned: {result}")
            return result
        except Exception as e:
            logger.error(f"Function {func.__name__} raised an exception: {e}")
            raise

    return wrapper
