1. test_add_new_book_invalid_name_len - негативная проверка - не добавлены книги с длиной названия более 40 символов (41, 68 символов)
2. test_set_book_genre_existed_book_existed_genre - позитивная проверка - устанавливлен жанр для книги: книга есть в books_genre, жанр входит в список genre
3. test_set_book_genre_existed_book_unexisted_genre - негативная проверка - не установлен жанр для книги: книга есть в books_genre, жанр не входит в список genre
4. test_get_book_genre_genre_included_in_books_genre - позитивная проверка - выведен жанр книги по её имени: книга и ее жанр есть в books_genre
5. test_get_books_with_specific_genre_two_books - позитивная проверка - выведен список из 2 книг по указанному жанру: книги и их жанр есть в books_genre
6. test_get_books_for_children_one_book - позитивная проверка - выведен список из 1 книги: книги и ее жанр есть в books_genre, жанр книги не входит в genre_age_rating
7. test_add_book_in_favorites_included_in_books_genre - позитивная проверка - добавлена в избранное одна книга: книга добавлена впервые, книга есть в books_genre
8. test_delete_book_from_favorites - позитивная проверка - удалена из избранного одна книга: книга была в избранном
9. test_get_list_of_favorites_books - позитивная проверка - выведено количество книг в избранном: указано количество книг, которые были были ранее добавлены в избранное