from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    import pytest
    @pytest.mark.parametrize('invalid_name', [
        'Гордость и предубеждение и зомби. Часть 2',
        'Длинное название, которое превышает максимальные количество символов'])
    
    def test_add_new_book_invalid_name_len(self, invalid_name):
        collector = BooksCollector()
        collector.add_new_book(invalid_name)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_existed_book_existed_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert collector.get_books_genre() == {'Что делать, если ваш кот хочет вас убить': 'Ужасы'}
        
    def test_set_book_genre_existed_book_unexisted_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Мелодрама')
        assert collector.get_books_genre() == {'Что делать, если ваш кот хочет вас убить': ''}
    
    def test_get_book_genre_genre_included_in_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') == 'Ужасы'

    def test_get_books_with_specific_genre_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']

    def test_get_books_for_children_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Ваш кот из семейки Аддамс')
        collector.set_book_genre('Ваш кот из семейки Аддамс', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Ваш кот из семейки Аддамс']

    def test_add_book_in_favorites_included_in_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.get_list_of_favorites_books() == ['Что делать, если ваш кот хочет вас убить']

    def test_delete_book_from_favorites_book_included_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')        
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Что делать, если ваш кот хочет вас убить']

    def test_get_list_of_favorites_books_two_added_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 2
