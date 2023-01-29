class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if isinstance(pages, int):
            if pages > 0:
                self.pages = pages
            else:
                raise ValueError(f'Некорректное число страниц: {pages!r}')
        else:
            raise ValueError(f'Некорректный формат страниц: {pages!r}')

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Страниц {self.pages}."


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if isinstance(duration, (float, int)):
            if duration > 0:
                self.duration = duration
            else:
                raise ValueError(f'Некорректное значение длительности: {duration!r}')
        else:
            raise ValueError(f'Некорректный формат длительности: {duration!r}')

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Длительность {self.duration} минут."
