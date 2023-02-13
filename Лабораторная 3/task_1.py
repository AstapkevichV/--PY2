class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """"Возвращает количество страниц."""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """"Устанавливает количество страниц."""
        if isinstance(new_pages, int):
            if new_pages > 0:
                self._pages = new_pages
            else:
                raise ValueError(f'Некорректное число страниц: {new_pages!r}')
        else:
            raise TypeError(f'Некорректный формат страниц: {new_pages!r}')

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}."


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """"Возвращает длительность."""
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """"Устанавливает длительность."""
        if isinstance(new_duration, (float, int)):
            if new_duration >= 0:
                self._duration = new_duration
            else:
                raise ValueError(f'Некорректное значение длительности: {new_duration!r}')
        else:
            raise ValueError(f'Некорректный формат длительности: {new_duration!r}')

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}."
