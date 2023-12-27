import random

# Функция для ввода чисел с клавиатуры

def get_numbers(number_count):
    numbers = []
    for _ in range(number_count):
        number = input("Введите число: ")
        try:
            numbers.append(int(number))
        except ValueError:
            print("Введено некорректное число")
            exit()
    return numbers

# Функция для генерации случайных чисел

def generate_numbers(number_count):
    numbers = []
    for _ in range(number_count):
        number = random.randint(0, 100)
        try:
            numbers.append(int(number))
        except ValueError:
            print("Сгенерировано некорректное число")
            exit()
    return numbers

# Выводим меню

print("Выберите способ генерации чисел:")
print("1 - Рандомная генерация")
print("0 - Ввод с клавиатуры")

# Получаем выбор пользователя

choice = int(input("Ваш выбор: "))

# Получаем количество чисел

number_count = int(input("Введите количество чисел: "))

# Генерируем список чисел в соответствии с выбором пользователя

if choice == 1:
    numbers = generate_numbers(number_count)
elif choice == 0:
    numbers = get_numbers(number_count)
else:
    print("Неверный выбор")
    exit()

# Выводим список в консоль

print("Исходный список:")
print(numbers)

# Переворачиваем список

numbers.reverse()

# Выводим список в консоль

print("Перевернутый список:")
print(numbers)
