disk_size_in_mib = 1.44
number_of_pages = 100
number_of_lines = 50
number_of_symbols = 25
weight_of_one_char = 4

QUANTITY_TO_TRANSFER = 1024

disk_size_in_b = disk_size_in_mib * QUANTITY_TO_TRANSFER ** 2

weight_of_one_line = number_of_symbols * weight_of_one_char
weight_of_one_page = number_of_lines * weight_of_one_line
weight_of_one_book = number_of_pages * weight_of_one_page

number_of_books_in_disk = int(disk_size_in_b // weight_of_one_book)

# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", number_of_books_in_disk)
