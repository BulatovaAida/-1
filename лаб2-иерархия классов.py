#Эта иерархия имеет три уровня:
#Базовый класс Servo описывает общие характеристики всех сервоприводов.
#Класс SyncServo описывает характеристики синхронных сервоприводов.
#Класс AsyncServo описывает характеристики асинхронных сервоприводов.
#Класс LinearServo описывает характеристики линейных сервоприводов.
#Все классы имеют три характеристики: угол поворота, скорость вращения и ускорение.
# Эти характеристики задаются в конструкторе класса.
#Классы SyncServo и AsyncServo также имеют дополнительную характеристику, специфичную для их типа.
# Класс SyncServo имеет характеристику pulse_width,
# класс AsyncServo имеет характеристику duty_cycle.
#Для всех классов реализованы магические методы __str__() и __repr__().
# Метод __str__() возвращает строковое представление экземпляра класса, предназначенное для чтения человеком.
# Метод __repr__() возвращает строковое представление экземпляра класса, предназначенное для интерпретации интерпретатором Python.
class Servo:
  #  """Базовый класс сервопривода."""

    def __init__(self, angle: float, speed: float, acceleration: float):
        self.angle = angle
        self.speed = speed
        self.acceleration = acceleration

    def __str__(self):
        return f"Servo(angle={self.angle}, speed={self.speed}, acceleration={self.acceleration})"

    def __repr__(self):
        return f"<Servo angle={self.angle}, speed={self.speed}, acceleration={self.acceleration}>"


class SyncServo(Servo):
   # """Синхронный сервопривод."""

    def __init__(self, angle: float, speed: float, acceleration: float, pulse_width: float):
        super().__init__(angle, speed, acceleration)
        self.pulse_width = pulse_width

    def __str__(self):
        return f"SyncServo(angle={self.angle}, speed={self.speed}, acceleration={self.acceleration}, pulse_width={self.pulse_width})"

    def __repr__(self):
        return f"<SyncServo angle={self.angle}, speed={self.speed}, acceleration={self.acceleration}, pulse_width={self.pulse_width}>"


class AsyncServo(Servo):
   # """Асинхронный сервопривод."""

    def __init__(self, angle: float, speed: float, acceleration: float, duty_cycle: float):
        super().__init__(angle, speed, acceleration)
        self.duty_cycle = duty_cycle

    def __str__(self):
        return f"AsyncServo(angle={self.angle}, speed={self.speed}, acceleration={self.acceleration}, duty_cycle={self.duty_cycle})"

    def __repr__(self):
        return f"<AsyncServo angle={self.angle}, speed={self.speed}, acceleration={self.acceleration}, duty_cycle={self.duty_cycle}>"


class LinearServo(Servo):
   # """Линейный сервопривод."""

    def __init__(self, angle: float, speed: float, acceleration: float, stroke: float):
        super().__init__(angle, speed, acceleration)
        self.stroke = stroke

    def __str__(self):
        return f"LinearServo(angle={self.angle}, speed={self.speed}, acceleration={self.acceleration}, stroke={self.stroke})"

    def __repr__(self):
        return f"<LinearServo angle={self.angle}, speed={self.speed}, acceleration={self.acceleration}, stroke={self.stroke}>"

#пример:

servo_1 = SyncServo(angle=90, speed=100, acceleration=1000,pulse_width=1000)
servo_2 = AsyncServo(angle=90, speed=100, acceleration=1000,duty_cycle=1000)

if servo_1 == servo_2:
    print("Сервоприводы равны")
else:
    print("Сервоприводы не равны")
