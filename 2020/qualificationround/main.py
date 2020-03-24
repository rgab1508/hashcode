f = open("inputs/c_incun.txt")

books_scanned = []
## Parsing inputs
l1 = f.readline().split(" ")
n_of_total_books, n_of_libs, n_of_days = int(l1[0]), int(l1[1]), int(l1[2])
# n_of_libs = 2
# n_of_days = 7

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
        'books': books_in_lib,
        'signed': False ,
        'books_scanned': []
    }
    libraries.append(lib)

# ## SORTING LIBRARY FROM LESS [TIME_TO_SIGN] TO MAX
libraries.sort(key=lambda x: x['time_to_sign'])
# print(libraries)

# libraries = [{'lib_id': 0, 'no_of_books': 5, 'time_to_sign': 2, 'books_shiped_in_day': 2, 'books': [0, 1, 2, 3, 4], 'signed': False, 
# 'books_scanned': []}, {'lib_id': 1, 'no_of_books': 4, 'time_to_sign': 3, 'books_shiped_in_day': 1, 'books': [0, 2, 3, 5], 'signed': False, 'books_scanned': []}]

## MAIN DAY LOOP
curr_lib_index_signing = 0
curr_time_taken_to_sign = libraries[curr_lib_index_signing]["time_to_sign"]

for day in range(n_of_days):
    curr_time_taken_to_sign -= 1

    #check everytime if a library is signed
    for l in libraries:
        if l["signed"] == True and (len(l["books"]) > l["books_shiped_in_day"]):
            no_of_books_signed = l["books_shiped_in_day"]
            # if signed removes no_of_booked_shiped_in_day from books in lib
            l["books_scanned"].append(l["books"][:no_of_books_signed])
            for i in range(no_of_books_signed):
                l["books"].pop(0)

    if curr_time_taken_to_sign == 0:
        libraries[curr_lib_index_signing]["signed"] = True
        if curr_lib_index_signing < n_of_libs-1:
            # next lib
            curr_lib_index_signing += 1
        curr_time_taken_to_sign = libraries[curr_lib_index_signing]["time_to_sign"]

    
libs_signed = curr_lib_index_signing
of = open("outputs/a_ouput.txt", "w+")
of.write(str(libs_signed + 1))
of.write("\n")
for l in range(libs_signed):
    li = libraries[l]
    __ = []
    for i in range(len(li["books_scanned"])):
        for j in range(li["books_shiped_in_day"]):
            __.append(str(li["books_scanned"][i][j]))

    of.write("{} {}".format(li["lib_id"], len(li["books_scanned"]) * li["books_shiped_in_day"]))
    of.write("\n")
    of.write(" ".join(__) + "\n")
    # if not l > libs_signed - 2:
    #     of.write("\n")

of.close()

