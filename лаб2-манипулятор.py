#Эта реализация имеет три уровня иерархии:
#Базовый класс Link описывает узел манипулятора.
#Класс Manipulator описывает манипулятор.
#Класс Manipulator перегружает оператор сложения, чтобы можно было объединять манипуляторы.
#Функция get_position() в классе Manipulator вычисляет позицию манипулятора в пространстве.
# Для этого она последовательно вычисляет позиции всех звеньев манипулятора, добавляя их друг к другу



import math

class Link:
   # """Узел манипулятора."""

    def __init__(self, length: float, offset: float):
        self.length = length
        self.offset = offset

    def get_position(self, angle: float) -> tuple:
     #   """Возвращает позицию узла в пространстве."""
        x = self.length * math.cos(angle)
        y = self.length * math.sin(angle)
        z = self.offset
        return x, y, z


class Manipulator:
    #"""Манипулятор."""

    def __init__(self, links: list):
        self.links = links

    def get_position(self, angles: list) -> tuple:
        #"""Возвращает позицию манипулятора в пространстве."""
        position = (0.0, 0.0, 0.0)
        for link, angle in zip(self.links, angles):
            position = link.get_position(angle) + position
        return position

    def __add__(self, other: "Manipulator") -> "Manipulator":
       # """Перегружает оператор сложения. Возвращает манипулятор с объединенными звеньями."""
        new_links = self.links + other.links
        return Manipulator(new_links)


if __name__ == "__main__":
    # Создаем звенья манипулятора
    link1 = Link(1.0, 0.0)
    link2 = Link(2.0, math.pi / 2.0)
    link3 = Link(3.0, math.pi)

    # Создаем манипулятор
    manipulator1 = Manipulator([link1, link2, link3])

    # Устанавливаем углы поворота звеньев
    angles = [math.pi / 4.0, math.pi / 2.0, math.pi / 3.0]

    # Получаем позицию манипулятора
    position = manipulator1.get_position(angles)

    # Создаем второй манипулятор
    manipulator2 = Manipulator([link1, link2, link3])

    # Объединяем манипуляторы
    manipulator3 = manipulator1 + manipulator2

    # Получаем позицию объединенного манипулятора
    position2 = manipulator3.get_position(angles)

    # Вот пример использования реализации:
    print(f"Позиция первого манипулятора: {position}")
    print(f"Позиция второго манипулятора: {position2}")

#Как видно из вывода, манипулятор перемещается в пространстве в соответствии с заданными углами поворота звеньев.