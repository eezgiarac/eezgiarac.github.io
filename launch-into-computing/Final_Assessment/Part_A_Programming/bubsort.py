# Bubble sort in Python

import time
def bubbleSort(array):

    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:

                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


 #data = [-2, 45, 0, 11, -9, 6, 99, 23, 18]



from pathlib import Path

file_path = Path(__file__).resolve().parent / "CPUPI.txt"

with open(file_path, "r") as file:
    numbers = [int(x) for x in file.read().split()]

 #data = numbers[:100]

data = numbers[:1000]
print("Number of elements:", len(data))

start = time.perf_counter()
bubbleSort(data)
end = time.perf_counter()

print("Sorted Array in Ascending Order:")
print(data)
print(f"Execution time: {end - start:.6f} seconds")