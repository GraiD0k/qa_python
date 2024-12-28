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
        collector.add_new_book('Война и Мир')
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
