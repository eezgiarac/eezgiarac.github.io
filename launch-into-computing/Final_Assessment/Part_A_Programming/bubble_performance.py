
from pathlib import Path
import time

# Bubble Sort algorithm
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

# Read the dataset
file_path = Path(__file__).resolve().parent / "CPUPI.txt"

with open(file_path, "r") as file:
    numbers = [int(x) for x in file.read().split()]

data = numbers[:1000]
times = []

# Repeat the test five times
for i in range(5):
    test_data = data.copy()

    start = time.perf_counter()
    bubbleSort(test_data)
    end = time.perf_counter()

    assert test_data == sorted(data), "Sorting failed!"

    execution_time = end - start
    times.append(execution_time)

    print(f"Test {i + 1}: {execution_time:.8f} seconds")

average_time = sum(times) / len(times)

print("Number of elements:", len(data))
print(f"Average execution time: {average_time:.8f} seconds")



import csv

with open("bubble_results.csv", "a", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["algorithm", "elements", "average_time"])
    writer.writerow(["Bubble Sort", len(data), average_time])

print("Results saved successfully!")

from pathlib import Path

print("CSV location:", Path("bubble_results.csv").resolve())