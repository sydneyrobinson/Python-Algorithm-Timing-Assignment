import timeit
import numpy as np
from numpy import average



my_setup= '''
import Array
from Array import array

the_array = array.copy()
n = len(the_array)

'''
#https://www.geeksforgeeks.org/python-check-if-list-is-sorted-or-not/
#code to check if list is sorted. ^^^

my_code= '''


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

 # See if left child of root exists and is
 # greater than root

    if l < n and arr[i] < arr[l]:
        largest = l

 # See if right child of root exists and is
 # greater than root

    if r < n and arr[largest] < arr[r]:
        largest = r

 # Change root, if needed

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap

  # Heapify the root.

        heapify(arr, n, largest)


# The main function to sort an array of given size

def heapSort(arr):
    n = len(arr)

 # Build a maxheap.
 # Since last parent will be at ((n//2)-1) we can start at that location.

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

 # One by one extract elements

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)


# Driver code to test above


heapSort(the_array)
#print(f"this is the copy: {the_array}")
#print(f"this is the actual array: {array}")
'''
trials = 1
repeats = 20
total_time = timeit.repeat(stmt = my_code, setup = my_setup, number = trials, repeat = repeats)
avg_time = average(timeit.repeat(stmt = my_code, setup = my_setup, number = trials, repeat = repeats))

global heapSort_max_time, heapSort_avg_time, heapSort_min_time

#time variables
max_time = max(total_time)
heapSort_max_time = max_time/trials

heapSort_avg_time = avg_time/trials

min_time = min(total_time)
heapSort_min_time = min_time/trials

#print(f"\nthis is heap sort total time: {total_time}")
print(f"\n~~~\nthis is heap sort min time: {heapSort_min_time}")
print(f"\nthis is heap sort average time: {heapSort_avg_time}")
print(f"\nthis is heap sort max time: {heapSort_max_time}")