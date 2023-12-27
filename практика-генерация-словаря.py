import random

# Функция для генерации словаря

def generate_dictionary(key_count, value_count):
    dictionary = {}
    for _ in range(key_count):
        key = random.choice(["a", "b", "c", "d", "e"])
        value = random.randint(1, 100)
        dictionary[key] = value
    return dictionary

# Функция для вывода словаря в консоль

def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")

# Функция для преобразования словаря в список кортежей

def convert_dictionary_to_list(dictionary):
    result = []
    for key, value in dictionary.items():
        if value not in result:
            result.append((value, [key]))
        else:
            result[result.index((value, [key]))][1].append(key)
    return result

# Выводим меню

print("Выберите способ генерации словаря:")
print("1 - Рандомная генерация")
print("0 - Ввод с клавиатуры")

# Получаем выбор пользователя

choice = int(input("Ваш выбор: "))

# Генерируем словарь

if choice == 1:
    dictionary = generate_dictionary(5, 10)
elif choice == 0:
    # Вводим количество ключей
    key_count = int(input("Введите количество ключей: "))

    # Вводим количество значений
    value_count = int(input("Введите количество значений: "))

    dictionary = {}
    for _ in range(key_count):
        key = input("Введите ключ: ")
        value = input("Введите значение: ")
        dictionary[key] = value
else:
    print("Неверный выбор")
    exit()

# Выводим словарь в консоль

print_dictionary(dictionary)

# Преобразуем словарь в список кортежей

result = convert_dictionary_to_list(dictionary)

# Выводим список кортежей в консоль

print(result)
