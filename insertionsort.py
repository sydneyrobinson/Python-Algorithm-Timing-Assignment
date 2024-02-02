import timeit
import numpy as np
from numpy import average
my_setup ='''
import Array 
from Array import array

the_array = array.copy()

'''


#b is the array
my_code = '''

def insertionSort(the_array):
    b = the_array[:]
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b
    
insertionSort(the_array)
#print(f"this is the copy: {the_array}")
#print(f"this is the actual array: {array}")
'''
#print(f"\nthis is insertion sort: {array}")

trials = 1
repeats = 20
total_time = timeit.repeat(stmt = my_code, setup = my_setup, number = trials, repeat = repeats)
avg_time = average(timeit.repeat(stmt = my_code, setup = my_setup, number = trials, repeat = repeats))

global insertionSort_max_time, insertionSort_avg_time, insertionSort_min_time

#time variables
max_time = max(total_time)
insertionSort_max_time = max_time/trials

insertionSort_avg_time = avg_time/trials

min_time = min(total_time)
insertionSort_min_time = min_time/trials
#print(f"\nthis is insertion sort total time: {total_time}")
print(f"\n~~~\nthis is insertion sort min time: {insertionSort_min_time}")
print(f"\nthis is heap sort average time: {insertionSort_avg_time}")
print(f"\nthis is heap sort max time: {insertionSort_max_time}")