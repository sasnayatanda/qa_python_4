from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollectors:
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('book_name', [
        'Мастер и Маргарита',
        'Аб' * 20,
        '1+1'
    ])
    def test_add_book_true_adds_to_genre(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    def test_add_book_false_add_to_genre_if_name_zero(self):
        collector = BooksCollector()
        name = ''
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_add_book_false_add_to_genre_if_name_41(self):
        collector = BooksCollector()
        name = 'А' * 41
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Комедии')
        assert 'Комедии' in collector.get_book_genre('Война и мир')

    @pytest.mark.parametrize('name', [
        'Мастер и Маргарита',
        'Привет, ревьювер :)',
        '1+1'
    ])
    def test_get_books_with_specific_genre(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Комедии')
        collector.set_book_genre(name, 'Комедии')
        collector.set_book_genre(name, 'Комедии')
        assert name in collector.get_books_with_specific_genre('Комедии')

    @pytest.mark.parametrize('name', [
        'Мастер и Маргарита',
        'Привет, ревьювер :)',
        '1+1'
    ])
    def test_get_books_for_children(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Комедии')
        collector.set_book_genre(name, 'Фантастика')
        collector.set_book_genre(name, 'Мультфильмы')
        assert name in collector.get_books_for_children()

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        name = 'Титаник'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert 'Титаник' in collector.favorites

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        name1 = 'Титаник'
        name2 = 'Война и мир'
        collector.add_new_book(name1)
        collector.add_book_in_favorites(name1)
        collector.add_book_in_favorites(name2)
        collector.delete_book_from_favorites(name1)
        assert name1 not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        books = ['Титаник', 'Война и мир', 'Легкий способ бросить курить']
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
        assert books == collector.get_list_of_favorites_books()

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Комедии')
        assert 'Комедии' in collector.get_book_genre('Война и мир')

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Отцы и дети')
        collector.set_book_genre('Война и мир', 'Комедии')
        collector.set_book_genre('Отцы и дети', 'Ужасы')
        assert {"Война и мир": "Комедии", "Отцы и дети": "Ужасы"} == collector.get_books_genre()
