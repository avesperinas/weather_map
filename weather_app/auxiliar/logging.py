"""Module for managing exceptions and logging errors."""


import os
import sys
import logging
from typing import Callable


def setup_logger() -> logging.Logger:

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    if not logger.handlers:
        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger


logger = setup_logger()


def manage_exception(function: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        
        if os.environ.get("MANAGE_EXCEPTIONS", "false") == "true":

            try:
                return function(*args, **kwargs)
            
            except Exception as e:
                log_exception_with_traceback(e)

            except SystemExit:
                raise
            
        else:
            return function(*args, **kwargs)

    return wrapper


def log_exception_with_traceback(exception: Exception) -> None:
    
    logger.error(f"Excepción: {str(exception)}")
    sys.exit(1)
