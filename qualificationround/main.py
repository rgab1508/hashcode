f = open("inputs/a_example.txt")

l1 = f.readline().split(" ")
n_of_total_books, n_of_libs, n_of_days = int(l1[0]), int(l1[1]), int(l1[2])

book_scores = f.readline().split(" ")

libraries = []

for i in range(n_of_libs):
    l1 = f.readline().split(" ")
    n_of_b, t_of_sign, books_shiped = int(l1[0]), int(l1[1]),int(l1[2])
    books_in_lib = [int(x) for x in f.readline().split(" ")]

    lib = {
        'lib_id':i,
        'no_of_books': n_of_b,
        'time_to_sign': t_of_sign,
        'books_shiped_in_day': books_shiped,
        'books': books_in_lib       
    }
    libraries.append(lib)

print(libraries)