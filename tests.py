from main import BooksCollector

import pytest


class TestBooksCollector:

    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.get_books_genre()
    
    @pytest.mark.parametrize("book_name", ["", "A" * 41])
    def test_add_new_book_invalid_name(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    def test_set_book_genre_valid_case(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Романтика')
        assert collector.get_book_genre('Гарри Поттер') == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Голодные игры')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Голодные игры', 'Фантастика')
        books = collector.get_books_with_specific_genre('Фантастика')
        assert books == ['Гарри Поттер', 'Голодные игры']

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Оно')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        books_for_children = collector.get_books_for_children()
        assert books_for_children == ['Гарри Поттер']

    def test_add_book_in_favorites_valid_case(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']

    def test_add_book_in_favorites_not_in_books_genre(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == []

    @pytest.mark.parametrize("book_name,expected_genre", [
        ("Гарри Поттер", ""),
        ("Голодные игры", "")
    ])
    def test_get_book_genre(self, book_name, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == expected_genre
