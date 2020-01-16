import os
import math
f = open('e_also_big.in', 'r')

#getting data
line1 = f.readline().split(' ')
MAX_SLICES,NO_OF_TYPES  =int(line1[0]),int(line1[1])


line2 = f.readline().split(' ')
slices = [int(x) for x in line2]



def find_lowest_mid(max_slices, _slices):
    _slices.reverse()
    for i in range(len(_slices)):
        if _slices[i] < max_slices:
            return i 

def mid_item(_MAX_SLICES, _slices):
    piz_ind = []
    slices_ord = []
    while(_MAX_SLICES >= _slices[0]):
        # print("in loop")
        mid_index = math.floor(len(_slices)/2)
        
        if(_slices[mid_index] > _MAX_SLICES):
            mid_index = find_lowest_mid(_MAX_SLICES, _slices)


        curr = _slices[mid_index]
        curr_poped = _slices.pop(mid_index)
        slices_ord.append(curr_poped)
        piz_ind.append(mid_index)
        # print(f'{_MAX_SLICES} : {curr_poped} :  {_slices}')

        _MAX_SLICES = _MAX_SLICES - curr

    
    return {'MAX_SLICES': _MAX_SLICES, 'slices_ord': slices_ord, 'piz_ind': piz_ind}

mid_item_output = mid_item(MAX_SLICES, slices)
print(sum(mid_item_output['slices_ord']))
print(mid_item_output['MAX_SLICES'])
# print(mid_item_output['piz_ind'])
# print(piz_ind)
# print(sum(slices_ord))



    





