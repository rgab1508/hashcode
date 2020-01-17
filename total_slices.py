files = ['a_example.in', 'b_small.in', 'c_medium.in', 'd_quite_big.in', 'e_also_big.in']
summ = 0

for f in files:
    ff = open(f)
    line = ff.readline().split(" ")
    summ += int(line[0])
    ff.close()


print(summ) 