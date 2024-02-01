import timeit

my_setup = '''
import main 
from main import array

the_array = array.copy()

N = len(the_array)
'''

my_code = '''

# Function to find the partition position
def partition(the_array, low, high):
    array = the_array[:]
    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)


# Driver code


# Function call
quicksort(the_array, 0, N - 1)
print(f"this is the copy: {the_array}")
print(f"this is the actual array: {array}")
'''
#print(f'\nthis is quicksort: {array}')

trials = 1
repeats = 1
total_time = timeit.repeat(stmt = my_code, setup = my_setup, number = trials, repeat = repeats)
min_time = min(total_time)

#print(f"\nthis is quick sort total time: {total_time}")
print(f"\nthis is quick sort min time: {min_time/trials}")