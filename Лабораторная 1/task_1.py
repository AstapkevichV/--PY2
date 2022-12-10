import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
class Seal:
    def __init__(self, color: str, weight: float):
        """
        Создание и подготовка к работе объекта "Тюлень"

        :param color: Окрас тюленя
        :param weight: Вес тюленя

        Примеры:
        >>> seal = Seal("gray", 130)
        """
        if not isinstance(color, str):
            raise TypeError('Цвет должен быть типа str')
        self.color = color

        if not isinstance(weight, (int, float)):
            raise TypeError('Вес должен быть типа int или float')
        if weight <= 0:
            raise ValueError('Вес должен быть положительным числом')
        self.weight = weight

    def eat(self, food_amount: float) -> None:
        """
        Процесс поглощения тюленем пищи.

        :param food_amount: Объем съеденной пищи(поглощенные калории)

        Примеры:
        >>> seal = Seal("gray", 100)
        >>> seal.eat(50)
        """
        if not isinstance(food_amount, (float, int)):
            raise TypeError('Объем еды должен быть типа float или int')
        if food_amount < 0:
            raise ValueError('Объем еды должен быть положительным числом')
        self.weight += food_amount

    def sleep(self, calories_burnt: float) -> None:
        """
        Потеря калорий во время сна.

        :param calories_burnt: Потерянные калории(сожженный вес)
        :raise ValueError: Если количество потерянных калорий превышает допустимое значение

        Примеры:
        >>> seal = Seal("brown", 150)
        >>> seal.sleep(30)
        """
        if not isinstance(calories_burnt, (float, int)):
            raise TypeError('Сожженные калории должны быть типа float или int')
        if calories_burnt < 0:
            raise ValueError('Сожженные калории должны быть положительным числом')
        if calories_burnt > 50:
            raise ValueError('Превышен лимит сожженых калорий')
        self.weight -= calories_burnt


class Tea:
    def __init__(self, type_: str, amount: float):
        """
        Создание и подготовка к работе объекта "Чай"

        :param type_: Сорт чая
        :param amount: Объем чая в коробке

        Примеры:
        >>> tea = Tea("green", 500)
        """
        if not isinstance(type_, str):
            raise TypeError('Сорт должен быть типа str')
        self.type_ = type_

        if not isinstance(amount, (int, float)):
            raise TypeError('Объем должен быть типа int или float')
        if amount <= 0:
            raise ValueError('Объем должен быть положительным числом')
        self.amount = amount

    def add_tea_to_box(self, additional_tea: float) -> None:
        """
        Добавление чая в коробку.

        :param additional_tea: Объем добавляемого чая

        Примеры:
        >>> tea = Tea("fruit", 150)
        >>> tea.add_tea_to_box(50)
        """
        if not isinstance(additional_tea, (float, int)):
            raise TypeError('Объем добавляемого чая должен быть типа float или int')
        if additional_tea < 0:
            raise ValueError('Объем добавляемого чая должен быть положительным числом')
        self.amount += additional_tea

    def is_box_empty(self) -> bool:
        """
        Проверка есть ли чай в коробке.

        :return: Является ли коробка пустой

        Примеры:
        >>> tea = Tea("black", 300)
        >>> tea.is_box_empty()
        """
        ...


class Roll:
    def __init__(self, type_: str, stuffing: float):
        """
        Создание и подготовка к работе объекта "Булочка"

        :param type_: Вид булочки
        :param stuffing: Объем начинки

        Примеры:
        >>> roll = Roll('roll', 60)
        """
        if not isinstance(type_, str):
            raise TypeError('Вид должен быть типа str')
        self.type_ = type_

        if not isinstance(stuffing, (int, float)):
            raise TypeError('Объем начинки должен быть типа int или float')
        if stuffing < 0:
            raise ValueError('Объем начинки должен быть положительным числом')
        self.stuffing = stuffing

    def add_additional_stuffing(self, additional_stuffing: float) -> None:
        """
        Добавление дополнительной начинки.

        :param additional_stuffing: Объем добавляемого чая

        Примеры:
        >>> roll = Roll("croissant", 15)
        >>> roll.add_additional_stuffing(10)
        """
        if not isinstance(additional_stuffing, (float, int)):
            raise TypeError('Объем добавляемой начинки должен быть типа float или int')
        if additional_stuffing <= 0:
            raise ValueError('Объем добавляемой начинки должен быть положительным числом')
        self.stuffing += additional_stuffing

    def is_there_stuffing(self) -> bool:
        """
        Проверка есть ли в булочке начинка.

        :return: Является ли булочка с начинкой

        Примеры:
        >>> roll = Roll('croissant', 0)
        >>> roll.is_there_stuffing()
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
