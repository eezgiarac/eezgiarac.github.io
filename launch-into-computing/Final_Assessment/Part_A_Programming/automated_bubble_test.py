
from pathlib import Path
import time

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

file_path = Path(__file__).resolve().parent / "CPUPI.txt"

with open(file_path, "r") as file:
    numbers = [int(x) for x in file.read().split()]

sizes = [1000, 2000, 5000]

for size in sizes:
    data = numbers[:size]
    times = []

    print(f"\nTesting {size} elements")

    for repeat in range(5):
        test_data = data.copy()

        start = time.perf_counter()
        bubbleSort(test_data)
        end = time.perf_counter()

        assert test_data == sorted(data), "Sorting failed!"

        execution_time = end - start
        times.append(execution_time)

        print(f"Run {repeat + 1}: {execution_time:.8f} seconds")

    average_time = sum(times) / len(times)

    print(f"Average: {average_time:.8f} seconds")
