import timeit
import numpy as np
import random
import csv
from random import sample

max_num = 9999
#!! max num cannot be greater than array size
arr_size = 700   

array = np.array(random.sample([x for x in range(0,max_num)],arr_size))
#print(array)


print("--------")


import bucketsort
import heapsort
import insertionsort
import quicksort



# Function to write a single row to the CSV file
def write_to_csv(file_path, data):
    with open(file_path, 'a', newline='') as csvfile:
        fieldnames =  ["Array Size", "Array Range", "Sorting Mehtod", "Min Tme", "Avg Time","Max Time"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writerow(data)
'''
# Your variable
my_variable = 42

# CSV file path
csv_file_path = 'my_data.csv'

# Write the variable to the CSV file
write_to_csv(csv_file_path, [my_variable])

# Add more rows later
additional_variables = [56, 78, 90]
write_to_csv(csv_file_path, additional_variables)

print(f"Variables have been written to {csv_file_path}")
'''