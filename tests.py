from main import BooksCollector
import pytest

class TestBooksCollector:
    @pytest.mark.parametrize('book_name', ['Самое большое название книги, которое было 123', ''])

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    @pytest.mark.parametrize('book_name', ['O', 'Евгений Онегин', 'Название,которое состоит из 39 символов'])
    def test_add_new_book(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.add_new_book('Война и Мир 1')
        assert len(collector.get_books_genre()) == 2
    def test_set_book_genre(self):
        collector = BooksCollector()
        book_name = 'Евгений Онегин'
        genre_name = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)
        assert collector.get_book_genre(book_name) == genre_name

    def test_set_book_genre_set_invalid_genre(self):
        collector = BooksCollector()
        book_name = 'Летят утки'
        genre_name = 'Животные'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)
        assert len(collector.get_book_genre(book_name)) == 0

    def test_get_book_genre(self):
        collector = BooksCollector()
        book_name = 'Десять негретят'
        genre_name = 'Детективы'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)
        assert collector.get_book_genre(book_name) == genre_name

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Антошка')
        collector.set_book_genre('Антошка', 'Мультфильмы')
        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Мультфильмы')
        assert len(collector.get_books_with_specific_genre('Мультфильмы')) == 2

    @pytest.mark.parametrize('book_name', ['Война и Мир том 1', 'Война и Мир том 2', 'Война и Мир том 3'])
    def test_get_books_genre(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фантастика')
        assert collector.get_books_genre().get(book_name) == collector.books_genre.get(book_name)

    @pytest.mark.parametrize('book_name,genre_name', [['Маугли', 'Мультфильмы'], ['Евротур', 'Комедии']])
    def test_get_books_for_children(self, book_name, genre_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)
        assert len(collector.get_books_for_children()) == 1

    @pytest.mark.parametrize('book_name,genre_name', [['Пила', 'Ужасы'],['Дарья Донцова', 'Детективы']])
    def test_get_books_for_children_neg(self, book_name, genre_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)
        assert len(collector.get_books_for_children()) == 0