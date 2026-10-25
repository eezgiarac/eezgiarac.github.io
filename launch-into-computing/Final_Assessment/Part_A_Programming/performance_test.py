

from pathlib import Path
import time

# Read the dataset
file_path = Path(__file__).resolve().parent / "CPUPI.txt"

with open(file_path, "r") as file:
    numbers = [int(x) for x in file.read().split()]

# Select the first 1,000 numbers
data = numbers[:1000]

times = []

# Repeat the test five times
for i in range(5):
    test_data = data.copy()

    start = time.perf_counter()
    sorted_data = sorted(test_data)
    end = time.perf_counter()

    execution_time = end - start
    times.append(execution_time)

    print(f"Test {i + 1}: {execution_time:.8f} seconds")

average_time = sum(times) / len(times)

print("Number of elements:", len(data))
print(f"Average execution time: {average_time:.8f} seconds")


import csv

with open("bubble_results.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timsort", len(data), average_time])

print("Timsort results saved successfully!")



