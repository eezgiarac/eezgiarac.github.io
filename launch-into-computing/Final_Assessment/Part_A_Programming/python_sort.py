
from pathlib import Path
import time

# Read the dataset
file_path = Path(__file__).resolve().parent / "CPUPI.txt"

with open(file_path, "r") as file:
    numbers = [int(x) for x in file.read().split()]

# Select the first 100 numbers
 #data = numbers[:100]
data = numbers[:1000]

# Measure sorting time
start = time.perf_counter()

sorted_data = sorted(data)

end = time.perf_counter()

print("Number of elements:", len(data))
print("Sorted Array in Ascending Order:")
print(sorted_data)
print(f"Execution time: {end - start:.6f} seconds")