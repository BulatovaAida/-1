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
    numbers1 = generate_numbers(number_count)

elif choice == 0:
    numbers1 = get_numbers(number_count)

else:
    print("Неверный выбор")
    exit()

# Выводим список в консоль

print("Первый список:")
print(numbers1)

# Выводим список в консоль

print("Второй список:")
numbers1.reverse()
numbers2 = numbers1
print(numbers2)

numbers1.reverse()

# Создаем новый список

new_numbers = []

# Циклически добавляем в новый список четные по индексу числа из первого списка и нечетные по индексу числа из второго списка

for i in range(len(numbers1)-1):
    if i % 2 == 0:
        new_numbers.append(numbers1[i+1])

numbers1.reverse()
numbers2=numbers1

for i in range(len(numbers2)):
    if i % 2 == 0:
        new_numbers.append(numbers2[i])

# Выводим новый список в консоль

print("Третий список:")
print(new_numbers)

new_numbers = set(new_numbers)

print("Третий список без повторений:")
print(new_numbers)