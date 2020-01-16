import math

f = open('e_also_big.in', 'r')

#getting data
line1 = f.readline().split(' ')
MAX_SLICES,NO_OF_TYPES  =int(line1[0]),int(line1[1])


line2 = f.readline().split(' ')
slices = [int(x) for x in line2]

def find_next_lowest_item(max_slices, _slices):
    _slices.reverse()
    for i in range(len(_slices)):
        if _slices[i] < max_slices:
            return i 


# Starting from the highest element
def highest_item(_max_slices, _slices):
    slices_ord = []
    piz_ind = []
    while(_max_slices >= _slices[0]):
        
        
        curr_index = len(_slices) - 1

        if _slices[curr_index] > _max_slices:
            curr_index = find_next_lowest_item(_max_slices, _slices)

        curr_item = _slices[curr_index]

        _max_slices = _max_slices- curr_item
        curr_poped = _slices.pop(curr_index)
        slices_ord.append(curr_poped)
        piz_ind.append(curr_index)

    return { "_MAX_SLICES": _max_slices, "piz_ind": piz_ind, "slices_ord": slices_ord}


hi = highest_item(MAX_SLICES, slices)
print(sum(hi['slices_ord']))
print(hi['_MAX_SLICES'])


