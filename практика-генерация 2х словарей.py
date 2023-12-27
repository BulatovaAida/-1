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

print("Выберите способ генерации 1-го словаря:")
print("1 - Рандомная генерация")
print("0 - Ввод с клавиатуры")

# Получаем выбор пользователя

choice1 = int(input("Ваш выбор: "))

# Генерируем словарь

if choice1 == 1:
    dictionary1 = generate_dictionary(5, 10)
elif choice1 == 0:
    # Вводим количество ключей
    key_count = int(input("Введите количество ключей: "))

    # Вводим количество значений
    value_count = int(input("Введите количество значений: "))

    dictionary1 = {}
    for _ in range(key_count):
        key = input("Введите ключ: ")
        value = input("Введите значение: ")
        dictionary1[key] = value
else:
    print("Неверный выбор")
    exit()

print("Первый словарь:")
print_dictionary(dictionary1)


print("Выберите способ генерации 2-го словаря:")
print("1 - Рандомная генерация")
print("0 - Ввод с клавиатуры")

# Получаем выбор пользователя

choice2 = int(input("Ваш выбор: "))

# Генерируем словарь

if choice2 == 1:
    dictionary2 = generate_dictionary(5, 10)
elif choice2 == 0:
    # Вводим количество ключей
    key_count1 = int(input("Введите количество ключей: "))

    # Вводим количество значений
    value_count1 = int(input("Введите количество значений: "))

    dictionary2 = {}
    for _ in range(key_count1):
        key = input("Введите ключ: ")
        value = input("Введите значение: ")
        dictionary2[key] = value
else:
    print("Неверный выбор")
    exit()


# Выводим словари в консоль


print("Второй словарь:")
print_dictionary(dictionary2)

# Находим пересечения множеств значений словарей

intersection = set(dictionary1.values()).intersection(set(dictionary2.values()))

# Создаем новый словарь, содержащий только те пары ключ-значение, значения из которых входит в пересечение

new_dictionary = {}
for key, value in dictionary1.items():
    if value in intersection:
        new_dictionary[key] = value

# Выводим новый словарь в консоль

if len(intersection) == 0:
    print("Нет общих элементов")
else:
    print("Новый словарь:")
    print_dictionary(new_dictionary)
