import timeit
import numpy as np
import random
import csv
from random import sample
import Array
from Array import arr_size, max_num


import heapsort
from heapsort import heapSort_max_time, heapSort_avg_time, heapSort_min_time
import insertionsort
from insertionsort import insertionSort_max_time, insertionSort_avg_time, insertionSort_min_time
import quicksort
from quicksort import quickSort_max_time, quickSort_avg_time, quickSort_min_time
import bucketsort
from bucketsort import bucketSort_max_time, bucketSort_avg_time, bucketSort_min_time

times = [
    {"Array Size": arr_size, "Array Range": max_num, "Sorting Method": "Heap Sort",
     "Min Time": heapSort_min_time,
     "Avg Time": heapSort_avg_time, "Max Time": heapSort_max_time},
    #

    {"Array Size": arr_size, "Array Range": max_num, "Sorting Method": "Insertion Sort",
     "Min Time": insertionSort_min_time,
     "Avg Time": insertionSort_avg_time, "Max Time": insertionSort_max_time},

    #
    {"Array Size": arr_size, "Array Range": max_num, "Sorting Method": "Quick Sort",
     "Min Time": quickSort_min_time,
     "Avg Time": quickSort_avg_time, "Max Time": quickSort_max_time},
    #
    {"Array Size": arr_size, "Array Range": max_num, "Sorting Method": "Bucket Sort",
     "Min Time": bucketSort_min_time,
     "Avg Time": bucketSort_avg_time, "Max Time": bucketSort_max_time}
]

def write_to_csv(file_path, data):
    with open(file_path, 'a', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


csv_file_path = 'my_data.csv'

write_to_csv(csv_file_path, times)

'''
# Your variable
my_variable = 42

# CSV file path


# Write the variable to the CSV file
write_to_csv(csv_file_path, [my_variable])

# Add more rows later
additional_variables = [56, 78, 90]
write_to_csv(csv_file_path, additional_variables)

print(f"Variables have been written to {csv_file_path}")
'''
