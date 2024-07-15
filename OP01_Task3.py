def calculator(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Devision by zero error"
    integer_division = a // b if b != 0 else "Devision by zero error"
    modulus = a % b if b != 0 else "Devision by zero error"
    exponentiation = a ** b

    return {
        "addition": addition,
        "subtraction": subtraction,
        "multiplication": multiplication,
        "division": division,
        "integer_division": integer_division,
        "modulus": modulus,
        "exponentiation": exponentiation
    }


a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

results = calculator(a, b)

print(f"Сложение: {results['addition']}")
print(f"Вычитание: {results['subtraction']}")
print(f"Умножение: {results['multiplication']}")
print(f"Деление: {results['division']}")
print(f"Целая часть от деления: {results['integer_division']}")
print(f"Остаток от деления: {results['modulus']}")
print(f"Возведение в степень: {results['exponentiation']}")