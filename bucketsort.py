import timeit

my_setup = '''
import main 
from main import array
from main import arr_size

the_array = array.copy()


No_Of_Buckets = 5
'''

#https://www.guru99.com/bucket-sort.html#:~:text=Method%202%3A%20Bucket%20Sort%20Algorithm%20for%20Integer%20Elements,-The%20bucket%20sort&text=Step%201)%20Find%20the%20maximum,initialize%20those%20buckets%20as%20empty.&text=Step%205)%20Sort%20each%20bucket,buckets%20into%20a%20single%20array.

my_code = '''

def bucketSort(the_array, No_Of_Buckets):
    
    max_element = max(the_array)
    min_element = min(the_array)
    span = (max_element - min_element) / No_Of_Buckets
    output = []
    for bucket in range(No_Of_Buckets):
        output.append([])
    for element in range(len(the_array)):
        diff = (the_array[element] - min_element) / span - int(
            (the_array[element] - min_element) / span
        )
        if diff == 0 and the_array[element] != min_element:
            output[int((the_array[element] - min_element) / span) - 1].append(
                the_array[element]
            )
        else:
            output[int((the_array[element] - min_element) / span)].append(the_array[element])
    for bucket in range(len(output)):
        if len(output[bucket]) != 0:
            output[bucket].sort()
    index = 0
    for bucket in output:
        if bucket:
            for element in bucket:
                the_array[index] = element
                index = index + 1


bucketSort(the_array, No_Of_Buckets)
#print(f"this is the copy: {the_array}")
#print(f"this is the actual array: {array}")
'''
#print("\nthis is bucket sort: ", the_array)

trials = 1
repeats = 20
total_time = timeit.repeat(stmt = my_code, setup = my_setup, number = trials, repeat = repeats)
min_time = min(total_time)
bucketSort_min_time = min_time/trials
#print(f"\nthis is bucket sort total time: {total_time}")
print(f"\nthis is bucket sort min time: {bucketSort_min_time}")