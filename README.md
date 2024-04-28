# Создание объекта вынесено фикстурой в конфтест


Проверяет словари конструктора при создании объекта
    test_books_genre_fav_dict_is_empty

Проверяет что у созданного объекта есть заполненный список с жанрами
    test_genre_list_is_not_empty

Проверяет что у созданного объекта есть список с жанрами 18+
    test_genre_age_rating_list_is_not_empty

Тест с параметризацией проверяет добавление новых книг в список 
    test_add_new_book_positive

Тест проверяет что книги с названиями 40+ символов не будут добавлены в список книг
    test_add_new_book_more_negative_sizes

Тест с параметризацией добавляет новые книги и проверяет задавание книгам жанров
    test_set_book_genre_valid_name

Тест проверяет возвращение жанра книги по названию
    test_get_book_genre_return_valid_name

Тест проверяет что выводится список книг по определенным жанрам.
    test_get_books_with_specific_genre_when_valid_genre

Тест проверяет что в список добавились все книги и что все они помещаются в словарь.
    test_get_books_genre_filled_dict

Тест проверяет что нельзя получить пустой список
    test_get_books_genre_empty_dict

 Тест проверяет что в списке с книгами есть только книги с рейтингом для детей.
    test_get_books_for_children_correct_genre

 Тест проверяет что книги с рейтингом жанров 18+ не попадают в список книг для детей.
    test_get_books_for_children_adult_rating

 Тест проверяет что книга добавленная в избранное есть в избранном 
    test_add_book_in_favorites_when_books_in_list

 Тест проверяет что нельзя добавить книгу в избранное, если её нет в списке книг.
    test_add_book_in_favorites_when_book_not_in_list

 Тест проверяет удаление книги из избранного.
    test_delete_book_from_favorites

 Тест проверяет что после удаления единственной книги из списка избранного, 
метод получения списка избранного вернет пустой список.
    test_get_list_of_favorites_books_empty_list
