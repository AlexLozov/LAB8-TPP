# simple calculator functions

def divide(a, b):
    """
    делит a на b и возвращает результат
    Искусственный баг: если b=0 возвращает 0 вместо ошибки
    """
    if b == 0:
        raise ZeroDivisionError("division by zero") # исправили баг
    return a / b