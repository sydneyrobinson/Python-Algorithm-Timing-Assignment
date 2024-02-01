import timeit
import numpy as np
import random
from random import sample

max_num = 9999
#!! max num cannot be greater than array size
arr_size = 700   

array = np.array(random.sample([x for x in range(0,max_num)],arr_size))
print(array)


print("--------")


import bucketsort
import heapsort
import insertionsort
import quicksort