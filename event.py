
from functools import wraps

events = dict()


def eventbus(event_type):

    def decorator(func):

        @wraps(func)
        def inner(*args, **kwargs):
            if event_type not in events:
                events[event_type] = list()
            events[event_type].append(func)
        inner()
        return inner

    return decorator
