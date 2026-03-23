from calculator import divide

def main():
    print("Пример работы калькулятора деления")
    a = float(input("Введите делимое: "))
    b = float(input("Введите делитель: "))
    result = divide(a, b)
    print(f"Результат деления: {result}")

if __name__ == "__main__":
    main()