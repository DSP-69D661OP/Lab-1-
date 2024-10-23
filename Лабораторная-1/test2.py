# TODO Найдите количество книг, которое можно разместить на дискете
number_of_pages = 100
number_of_rows = 50
number_of_characters = 25
symbol_size = 4
size_lbcrtns = 1024 * 1024 * 1.44

book_symbols = number_of_characters * number_of_rows * number_of_pages
book_size = book_symbols * 4

books = size_lbcrtns // book_size
print("Количество книг, помещающихся на дискету:",int(books))
