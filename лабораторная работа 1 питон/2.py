# TODO Найдите количество книг, которое можно разместить на дискете
storage = 1.44
book = (4 * 25 * 50 * 100)
storage_book_mb = book / (1024 ** 2)
f = storage / storage_book_mb
print("Количество книг, помещающихся на дискету:", int(f))
