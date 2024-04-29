import random
import pytest


class TestBooksCollector:

    def test_books_genre_fav_dict_is_empty(self, books_collector):

        assert len(books_collector.get_list_of_favorites_books()) == 0

    def test_genre_list_is_not_empty(self, books_collector):

        assert books_collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating_list_is_not_empty(self, books_collector):

        assert books_collector.genre_age_rating == ['Ужасы', 'Детективы']

    @pytest.mark.parametrize('book', ['Мстители', 'Пуп земли'])
    def test_add_new_book_positive(self, books_collector, book):

        books_collector.add_new_book(book)
        assert books_collector.get_book_genre(book) == ''

    @pytest.mark.parametrize('book', ['', 'Очень длинный фильм про мстителей и как они мстят друг другу и остальным'])
    def test_add_new_book_more_negative_sizes(self, books_collector, book):

        assert not books_collector.add_new_book(book)

    def test_set_book_genre_valid_name(self, books_collector):

        books_collector.add_new_book('Найти, кому мстить')
        books_collector.set_book_genre('Найти, кому мстить', 'Детективы')
        assert books_collector.get_book_genre('Найти, кому мстить') == 'Детективы'

    def test_get_books_with_specific_genre_when_valid_genre(self, books_collector):

        books_collector.add_new_book('Котопес')
        books_collector.set_book_genre('Котопес', 'Мультфильмы')
        assert books_collector.get_books_with_specific_genre('Мультфильмы') \
               and type(books_collector.get_books_with_specific_genre('Мультфильмы')) == list


    def test_get_books_genre_filled_dict(self, books_collector):

        books = ['Котопес', 'Песокот', 'Мой брат Юлий', 'Первый под землей']
        for name in books:
            books_collector.add_new_book(name)

        random_book = random.choice(books)
        assert random_book in books_collector.get_books_genre() \
            and type(books_collector.get_books_genre()) == dict

    def test_get_books_genre_empty_dict(self, books_collector):

        assert not books_collector.get_books_genre()

    def test_get_books_for_children_correct_genre(self, books_collector):

        books = ['Салат в кармане', 'Сиреневыый туман', 'Сильный и слабый', 'Сегодня ко второй', 'Уволили']
        x = 0
        for name in books:
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, books_collector.genre[x])
            x += 1

        for genre in books_collector.genre_age_rating:
            for book in books_collector.get_books_with_specific_genre(genre):
                assert book not in books_collector.get_books_for_children()

    def test_get_books_for_children_adult_rating(self, books_collector):

        books = ['Дюймовочка', 'Снежная королева']
        x = 0
        for name in books:
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, books_collector.genre_age_rating[x])
            x += 1

        assert not books_collector.get_books_for_children()

    def test_add_book_in_favorites_when_books_in_list(self, books_collector):

        books_collector.add_new_book('Силомер')
        books_collector.add_book_in_favorites('Силомер')

        assert 'Силомер' in books_collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, books_collector):

        books_collector.add_new_book('Узколобый Джо')
        books_collector.add_book_in_favorites('Узколобый Джо')

        books_collector.delete_book_from_favorites('Узколобый Джо')
        assert 'Узколобый Джо' not in books_collector.get_list_of_favorites_books()


    