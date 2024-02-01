import timeit

my_setup ='''
import main 
from main import array

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
min_time = min(total_time)

#print(f"\nthis is insertion sort total time: {total_time}")
print(f"\nthis is insertion sort min time: {min_time/trials}")