class Calculator:
    @classmethod
    def sum(cls, a, b):
        return a + b

    @classmethod
    def subtract(cls, a, b):
        return a - b

    @classmethod
    def multiply(cls, a, b):
        return a * b

    @classmethod
    def divide(cls, a, b):
        if b == 0:
            raise ValueError("Деление на ноль недопустимо")
        return a / b

OPERATORS_NUM = {
    "+": Calculator.sum,
    "-": Calculator.subtract,
    "*": Calculator.multiply,
    "/": Calculator.divide
}

try:
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    action = input("Выберите действие (+, -, *, /): ")

    if action not in OPERATORS_NUM:
        raise ValueError("Неверное действие")

    result = OPERATORS_NUM[action](x, y)
    print(f"Результат: {result}")
except ValueError as e:
    print(f"Ошибка: {e}")
except ZeroDivisionError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
