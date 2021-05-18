from datetime import datetime
import functools


def apenas_horario_comercial(func):
    @functools.wraps(func)
    def wrapper():
        if datetime.now().hour >= 8 and datetime.now().hour <= 18:
            func()
        else:
            pass
    return wrapper


def duplicar(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


def titulo(mostrar):
    def decorator_titulo(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if mostrar:
                print("*"*20)
            return func(*args, **kwargs)
        return wrapper
    return decorator_titulo
