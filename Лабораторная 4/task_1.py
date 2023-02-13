if __name__ == "__main__":
    class Seal:
        """"Базовый класс тюленей."""
        HEAVY_WEIGHT = 300

        def __init__(self, species: str, weight: float, length: float):
            """
            Создание и подготовка к работе объекта "Тюлень"

            :param species: Вид тюленя
            :param weight: Вес тюленя в кг
            :param length: Вес тюленя в метрах

            Пример:
            >>> seal = Seal("Monk seal", 230, 2.4)  #Инициализация объекта класса
            """
            self._species = species
            self._weight = weight
            self._length = length

        @property
        def species(self) -> str:
            """Возвращает вид тюленя"""
            return self._species

        @property
        def weight(self) -> float:
            """Возвращает вес тюленя"""
            return self._weight

        @property
        def length(self) -> float:
            """Возвращает длину тюленя"""
            return self._length

        def check_weight(self, weight_: float) -> None:
            """"Проверяет, является ли формат и значение веса корректным"""
            if isinstance(weight_, (float, int)):
                if weight_ > 0:
                    self._weight = weight_
                else:
                    raise ValueError(f'Некорректное значение веса: {weight_!r}')
            else:
                raise TypeError(f'Некорректный формат веса: {weight_!r}')

        def check_length(self, length_: float) -> None:
            """"Проверяет, является ли формат и значение длины корректным"""
            if isinstance(length_, (float, int)):
                if length_ > 0:
                    self._length = length_
                else:
                    raise ValueError(f'Некорректное значение длины: {length_!r}')
            else:
                raise TypeError(f'Некорректный формат длины: {length_!r}')

        def __str__(self):
            """"Реализация магического метода __str__"""
            return f"Вид : {self.species}. Вес : {self.weight}. Длина : {self.length}"

        def __repr__(self):
            """"Реализация магического метода __repr__"""
            return f"{self.__class__.__name__}(species={self.species!r}, weight={self.weight!r}), length={self.length!r})"

        def is_heavy(self) -> bool:
            """Возвращает тяжелый тюлень или нет"""
            return self._weight > 300

        @staticmethod
        def habitat() -> str:
            """Возвращает предпочитаемое место обитания большинства видов."""
            return "Тюлени в большинстве своем предпочитают жить у морей и океанов."

    class ArcticSeal(Seal):
        """"Дочерний класс Арктический тюлень"""
        def __init__(self, species: str, weight: float, length: float, population: int):
            super().__init__(species, weight, length)
            self._population = population

        def __str__(self) -> str:
            """"Перегружаем метод, так как добавились новые атрибуты."""
            return f"Вид : {self.species}. Вес : {self.weight}. Длина : {self.length}. Популяция: {self.population}"

        @property
        def population(self) -> int:
            """"Возвращает количество особей."""
            return self._population

        @population.setter
        def population(self, new_population: int) -> None:
            """"Устанавливает количество страниц."""
            if isinstance(new_population, int):
                if new_population > 0:
                    self._population = new_population
                else:
                    raise ValueError(f'Некорректное число особей: {new_population!r}')
            else:
                raise TypeError(f'Некорректный формат особей: {new_population!r}')

        @staticmethod
        def habitat() -> str:
            """Перегружаем метод, чтобы отразить специфику области проживания отдельного вида."""
            return "Арктические тюление предпочитают жить в холодных водах."

    pass
