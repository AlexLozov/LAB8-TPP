# simple calculator functions

def divide(a, b):
    """
    делит a на b и возвращает результат
    Искусственный баг: если b=0 возвращает 0 вместо ошибки
    """
    if b == 0:
        return 0  # баг: должно быть raise ZeroDivisionError
    return a / b