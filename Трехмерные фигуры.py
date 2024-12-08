# ЗАДАЧА 1

'''

class Counter:
    def __init__(self, start=0):
        if start < 0:
            raise ValueError("Начальное значение счетчика не может быть отрицательным.")
        self.value = start

    def inc(self, amount=1):
        if amount < 0:
            raise ValueError("Количество для увеличения не может быть отрицательным.")
        self.value += amount

    def dec(self, amount=1):
        if amount < 0:
            raise ValueError("Количество для уменьшения не может быть отрицательным.")
        self.value = max(0, self.value - amount)


class NonDecCounter(Counter):
    def dec(self, amount=1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        super().__init__(start)
        if limit < 0:
            raise ValueError("Лимит не может быть отрицательным.")
        self.limit = limit

    def inc(self, amount=1):
        if amount < 0:
            raise ValueError("Количество для увеличения не может быть отрицательным.")
        self.value = min(self.value + amount, self.limit)


if __name__ == "__main__":
    counter = Counter(5)
    print(f"Counter value: {counter.value}")  # Вывод: 5
    counter.inc(3) # +3
    print(f"Counter after inc: {counter.value}")  # Вывод: 8
    counter.dec(2) #-2
    print(f"Counter after dec: {counter.value}")  # Вывод: 6

    non_dec_counter = NonDecCounter(5)
    print(f"NonDecCounter value: {non_dec_counter.value}")  # Вывод: 5
    non_dec_counter.inc(3) # +3
    print(f"NonDecCounter after inc: {non_dec_counter.value}")  # Вывод: 8
    non_dec_counter.dec(2)  # dec ничего не делает
    print(f"NonDecCounter after dec: {non_dec_counter.value}")  # Вывод: 8

    limited_counter = LimitedCounter(5, 10)
    print(f"LimitedCounter value: {limited_counter.value}")  # Вывод: 5
    limited_counter.inc(3) # +3
    print(f"LimitedCounter after inc: {limited_counter.value}")  # Вывод: 8
    limited_counter.inc(5) # +5, но лимит 10
    print(f"LimitedCounter after inc: {limited_counter.value}")  # Вывод: 10

'''

# ЗАДАЧА 2

'''

class Bachelor:
    def __init__(self, first_name, last_name, group, average_mark):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.average_mark = average_mark

    def get_scholarship(self):
        if self.average_mark == 5:
            return 10000
        elif self.average_mark > 3:
            return 5000
        else:
            return 0


class Undergraduate(Bachelor):
    def __init__(self, first_name, last_name, group, average_mark, research_work):
        super().__init__(first_name, last_name, group, average_mark)
        self.research_work = research_work

    def get_scholarship(self):
        if self.average_mark == 5:
            return 15000
        elif self.average_mark > 3:
            return 7500
        else:
            return 0


if __name__ == "__main__":
    students = [
        Bachelor("Иван", "Иванов", "Группа 1", 4.5),
        Bachelor("Петр", "Петров", "Группа 2", 2.8),
        Undergraduate("Светлана", "Сидорова", "Группа 3", 5.0, "Научная работа 1"),
        Undergraduate("Алексей", "Алексеев", "Группа 4", 3.5, "Научная работа 2"),
    ]

    for student in students:
        print(f"{student.first_name} {student.last_name}: Стипендия = {student.get_scholarship()} р.")

'''

# ЗАДАЧА 3

'''

class Product:
    def __init__(self, name, price, weight):
        self.__name = name
        self.__price = price
        self.__weight = weight

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight


class Buy(Product):
    def __init__(self, name, price, weight, quantity):
        super().__init__(name, price, weight)
        self.__quantity = quantity
        self.__total_price = self.calculate_total_price()
        self.__total_weight = self.calculate_total_weight()

    def set_quantity(self, quantity):
        self.__quantity = quantity
        self.__total_price = self.calculate_total_price()
        self.__total_weight = self.calculate_total_weight()

    def get_quantity(self):
        return self.__quantity

    def calculate_total_price(self):
        return self.get_price() * self.__quantity

    def calculate_total_weight(self):
        return self.get_weight() * self.__quantity


class Check(Buy):
    def __init__(self, name, price, weight, quantity):
        super().__init__(name, price, weight, quantity)

    def print_receipt(self):
        print(f"Product: {self.get_name()}")
        print(f"Price per unit: {self.get_price()}")
        print(f"Weight per unit: {self.get_weight()}")
        print(f"Quantity: {self.get_quantity()}")
        print(f"Total Price: {self._Buy__total_price}")
        print(f"Total Weight: {self._Buy__total_weight}")


if __name__ == "__main__":
    check = Check("Apple", 10, 0.2, 5)
    check.print_receipt()

'''

# ЗАДАЧА 4

'''

import math


class Shape:
    def surface_area(self):
        raise NotImplementedError("Этот метод должен быть переопределен.")

    def volume(self):
        raise NotImplementedError("Этот метод должен быть переопределен.")


class Cube(Shape):
    def __init__(self, side):
        self.side = side

    def surface_area(self):
        return 6 * (self.side ** 2)

    def volume(self):
        return self.side ** 3


class Sphere(Shape):
    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        return 4 * math.pi * (self.radius ** 2)

    def volume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)


class Cylinder(Shape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * (self.radius ** 2) * self.height


class RectangularPrism(Shape):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def surface_area(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)

    def volume(self):
        return self.length * self.width * self.height


class Ellipsoid(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def surface_area(self):
        p = 1.6075
        return 4 * math.pi * ((self.a * self.b) ** p + (self.a * self.c) ** p + (self.b * self.c) ** p) ** (1 / p)

    def volume(self):
        return (4 / 3) * math.pi * self.a * self.b * self.c


def check_shapes(shapes):
    total_volume = sum(shape.volume() for shape in shapes)
    print(f"Общий объем всех фигур: {total_volume}")  # Для отладки
    for shape in shapes:
        surface_area = shape.surface_area()
        volume = shape.volume()
        print(f"{shape.__class__.__name__}: Площадь поверхности = {surface_area}, Объем = {volume}")

    print("\nФигуры с объемом, равным или большему суммарному объему остальных фигур:")
    for shape in shapes:
        if shape.volume() >= total_volume - shape.volume():
            print(f"{shape.__class__.__name__}: Объем = {shape.volume()}, Площадь поверхности = {shape.surface_area()}")
        else:
            print("Нет")

if __name__ == "__main__":
    shapes = [
        Cube(3),
        Sphere(2),
        Cylinder(1, 5),
        RectangularPrism(2, 3, 4),
        Ellipsoid(1, 2, 3)
    ]

    check_shapes(shapes)

'''