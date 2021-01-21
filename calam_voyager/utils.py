import asyncio
from functools import wraps
from typing import Callable
from unittest import TestCase


def async_test(func):
    """Utility decorator for making async testing function run-able in `unittest.TestCase`."""
    
    @wraps(func)
    def inner(self: TestCase, *args, **kwargs):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(func(self, *args, **kwargs))
    return inner


def test_requires(*requirements: str):
    """Utility decorator for requiring any number of attributes exist and not be none when running a test with `unittest.TestCase`."""

    def wrapper(func: Callable):
        @wraps(func)
        def inner(self: TestCase, *args, **kwargs):
            missing_requirements = [(req, getattr(self, req, None) is None) for req in requirements]
            if any((is_missing for _, is_missing in missing_requirements)):
                raise ValueError('Test is missing required values: ' + ', '.join((req for req, is_missing in missing_requirements if is_missing)))
            else:
                return func(self, *args, **kwargs)
        return inner
    return wrapper
