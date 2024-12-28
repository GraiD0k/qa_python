test_add_new_book_add_invalid_len_name (Негативный) - тест проверяет, что метод add_new_book не работает, если в него передать пустоту или 40 символов
test_add_new_book (Позитивный) - Добавление книги в метод add_new_book 
test_add_new_book_add_two_books (Позитивный) - Одновременно добавляем две книги в метод add_new_book 
test_set_book_genre (Позитивный) - Установка жанра

test_set_book_genre_set_invalid_genre (Негативный) - Устанавливаем недопустимый жанр через метод set_book_genre
test_get_book_genre (Позитивный)  - Проверка метода get_book_genre
test_get_books_with_specific_genre (Позитивный) - Проверяем метод test_get_books_with_specific_genre
test_get_books_for_children (Позитивный) - Проверяет метод get_books_for_children
test_get_books_for_children_neg (Негативный) - Проверяет, что метод get_books_for_children не возвращает книги, которые недоступны детям
test_add_book_in_favorites (Позитивный) - Добавление книги в избранное с помощью метода add_book_in_favorites
test_add_book_in_favorites_add_two_equal_books (Негативный) - Пробуем добавить одну книгу два раза в избранное с помощью метода add_book_in_favorites 
test_delete_book_from_favorites (Позитивный) - Удаление из избранного с помощью метода delete_book_from_favorites 
test_get_list_of_favorites_books (Позитивный)-  Проверка метод get_list_of_favorites_books