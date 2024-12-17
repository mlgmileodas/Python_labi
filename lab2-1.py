import doctest

class Car:
    """Класс, описывающий автомобиль."""

    def __init__(self, model: str, max_speed: int) -> None:
        if not model:
            raise ValueError("Отсутствует название модели.")
        if not isinstance(max_speed, (int, float)) or max_speed <= 0:
            raise ValueError("Максимальная скорость может быть только положительного числа.")

    def start_engine(self) -> None:
        """Запускает двигатель."""
        # ... реализация запуска двигателя ...
        pass

    def accelerate(self, speed_increase: int) -> None:
        """
        Увеличивает скорость.

            speed_increase: Прирост скорости (неотрицательное число).
            ValueError: Если speed_increase отрицательно.

        """
        if not isinstance(speed_increase, (int, float)) or speed_increase < 0:
            raise ValueError("Скорость не может быть отрицательным числом.")
        # ... реализация увеличения скорости ...


class Shape:
    """Класс, описывающий геометрическую фигуру."""

    def __init__(self, name: str, num_sides: int) -> None:
        """
            name: Название фигуры (строка, не пустая).
            num_sides: Количество сторон (неотрицательное целое число).

            ValueError: Если num_sides отрицательное число или name пустая строка.
        """
        if not name:
            raise ValueError("Не введено имя.")
        if not isinstance(num_sides, int) or num_sides < 0:
            raise ValueError("Количество сторон не может быть отрицательным либо не целым числом.")

    def calculate_area(self) -> float:
        """Вычисляет площадь фигуры."""
        # ... реализация вычисления площади ...

    def calculate_perimeter(self) -> float:
        """
        Вычисляет периметр фигуры.
        """

class House:
    """Класс, описывающий дом."""

    def __init__(self, address: str, num_rooms: int) -> None:
        """
        address: Адрес дома (строка, не пустая).
        num_rooms: Количество комнат (положительное целое число).
        ValueError: Если num_rooms не положительное число или address пустая строка.
        """
        if not address:
            raise ValueError("Не введен адрес.")
        if not isinstance(num_rooms, int) or num_rooms <= 0:
            raise ValueError("Количество комнат не может быть отрицательным числом.")

    def add_room(self, room_type: str) -> None:
        """Добавляет комнату в дом."""

    def get_address(self) -> str:
        """
        Возвращает адрес дома.

        """
if __name__ == "__main__":
    doctest.testmod()