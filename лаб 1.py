import doctest


class Printer:
    def init(self, brand: str, max_pages_per_minute: int):
        if max_pages_per_minute <= 0:
            raise ValueError("Максимальная скорость печати должна быть больше 0.")
        self.brand = brand
        self.max_pages_per_minute = max_pages_per_minute

    def print_document(self, pages: int) -> None:
        """
        Печатает документ.

        :param pages: int Количество страниц для печати
        :raises ValueError: если количество страниц <= 0

        >>> printer = SomePrinter("HP", 30)
        >>> printer.print_document(10)
        """
        ...

    def check_ink_level(self) -> float:
        """
        Проверяет уровень чернил в принтере.

        :return: float Уровень чернил в процентах

        >>> printer = SomePrinter("Canon", 20)
        >>> printer.check_ink_level()
        75.0
        """
        ...

class Dog:
    def init(self, breed: str, age: int):
        if age < 0:
            raise ValueError("Возраст собаки не может быть отрицательным.")
        self.breed = breed
        self.age = age

    def bark(self) -> None:
        """
        Собака лает.

        >>> dog = SomeDog("Labrador", 3)
        >>> dog.bark()
        """
        ...


    def fetch(self, item: str) -> str:
        """
        Собака приносит указанный предмет.

        :param item: str Название предмета
        :return: str Сообщение о том, что собака принесла предмет

        >>> dog = SomeDog("Beagle", 2)
        >>> dog.fetch("мячик")
        'Собака принесла мячик.'
        """
        ...

class ReinforcedConcrete:
    def init(self, strength: float, density: float):
        if strength <= 0:
            raise ValueError("Прочность должна быть больше 0.")
        if density <= 0:
            raise ValueError("Плотность должна быть больше 0.")
        self.strength = strength
        self.density = density

    def calculate_load_capacity(self) -> float:
        """
        Рассчитывает грузоподъемность железобетона.

        :return: float Грузоподъемность в килограммах

        >>> concrete = SomeConcrete(300, 2400)
        >>> concrete.calculate_load_capacity()
        15000.0
        """
        ...

    def check_crack_resistance(self, load: float) -> bool:
        """
        Проверяет устойчивость к трещинам под нагрузкой.

        :param load: float Нагрузка в килограммах
        :return: bool True, если устойчивость к трещинам достаточна, иначе False

        >>> concrete = SomeConcrete(400, 2500)
        >>> concrete.check_crack_resistance(10000)
        True
        """
        ...

if name == "main":
    doctest.testmod()  # тестирование примеров, которые находятся в документации