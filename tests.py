import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_one_book_without_genre_added(self, collector):

        collector.add_new_book("Книга_1")

        assert "Книга_1" in collector.books_genre

        assert collector.books_genre.get("Книга_1") == ''

    @pytest.mark.parametrize("book_name, genre", [
        ("Книга_1", "Ужасы"),
        ("Книга_2", "Комедии"),
        ("Книга_3", "Мультфильмы"),
    ])
    def test_set_book_genre_string_set_genre(self, collector, book_name, genre):

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert collector.books_genre.get(book_name) == genre

    @pytest.mark.parametrize("book_name, expected_genre", [
        ("Книга_1", "Ужасы"),
        ("Книга_2", "Комедии"),
    ])
    def test_get_book_genre_book_name_get_genre(self, collector, book_name, expected_genre):

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, expected_genre)
        assert collector.get_book_genre(book_name) == expected_genre

    def test_get_books_with_specific_genre_get_list(self, collector):

        collector.add_new_book("Книга_1")
        collector.set_book_genre("Книга_1", 'Ужасы')

        assert collector.get_books_with_specific_genre('Ужасы') == ["Книга_1"]

    def test_get_books_genre(self, collector):

        collector.add_new_book("Книга_1")
        collector.set_book_genre("Книга_1", 'Ужасы')

        assert collector.get_books_genre != {}

        assert "Книга_1" in collector.get_books_genre()

    def test_get_books_for_children_return_books_for_children(self, collector):

        collector.add_new_book("Книга_1")
        collector.set_book_genre("Книга_1", 'Ужасы')
        collector.add_new_book("Книга_2")
        collector.set_book_genre("Книга_2", 'Комедии')

        assert "Книга_2" in collector.get_books_for_children()

    def test_add_book_in_favorites_name_book_added(self, collector):

        collector.add_new_book("Книга_2")
        collector.set_book_genre("Книга_2", 'Комедии')
        collector.add_book_in_favorites("Книга_2")

        assert "Книга_2" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_name_book_delete_book(self, collector):

        collector.add_new_book("Книга_2")
        collector.set_book_genre("Книга_2", 'Комедии')
        collector.add_book_in_favorites("Книга_2")
        collector.delete_book_from_favorites("Книга_2")

        assert collector.favorites == []
