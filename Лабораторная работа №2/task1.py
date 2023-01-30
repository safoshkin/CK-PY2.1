class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError('Идентификатор книги должен быть типа int')
        if id_ <= 0:
            raise ValueError('Идентификатор книги должен быть положительным числом')
        if not isinstance(name, str):
            raise TypeError('Идентификатор книги должен быть типа str')
        if not isinstance(pages, int):
            raise TypeError('Количество страниц в книге должено быть типа int')
        if pages <= 0:
            raise ValueError('Количество страниц в книге должено быть положительным числом')
        self.id = id_
        self.name = name
        self.page = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.page!r})'


class Library:
    def __init__(self, books: list[Book] = None):
        self.books = books
        if books is None:
            self.books = []

    def get_next_book_id(self) -> int:
        if self.books == []:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, id_: int) -> int:
        status = False
        index_book = 0
        for new_book in self.books:
            if new_book.id == id_:
                index_book = self.books.index(new_book)
                status = True
        if status:
            return index_book
        else:
            raise ValueError('Ни одна книга не соответствует запрашиваемому id_')


LIBRARY = [{"id_": 1, "name": "Пушкин А.С.", "pages": 600}, {"id_": 2, "name": "Есенин С.А.", "pages": 300}]

if __name__ == '__main__':
    print(Library().get_next_book_id())  # для пустой библиотеки

    list_books = [Book(id_=cur_book["id_"], name=cur_book["name"], pages=cur_book["pages"]) for cur_book in LIBRARY]
    print(Library(list_books).get_next_book_id())  # для непустой библиотеки

    print(Library(list_books).get_index_by_book_id(2))  # проверяем индекс книги с id = 2
