import sys
import time
import csv
from pathlib import Path


TEST_RUNS = 5


def bubble_sort(numbers):
    """Sort a list in ascending order using Bubble Sort."""

    data = numbers.copy()
    n = len(data)

    for step in range(n - 1):

        for i in range(n - step - 1):

            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]

    return data


def load_numbers(filename, limit):
    """Read the requested number of integers from CPUPI.txt."""

    numbers = []

    with open(filename, "r") as file:

        for line in file:

            for value in line.split():

                numbers.append(int(value))

                if len(numbers) == limit:
                    return numbers

    return numbers


def benchmark_sort(name, sort_function, numbers):
    """Run a sorting algorithm five times and calculate the average."""

    times = []
    final_result = None

    print(f"\n{name}")
    print("-" * 40)

    for run in range(TEST_RUNS):

        # Each run starts with the same unsorted data
        test_data = numbers.copy()

        # Start timing
        start = time.perf_counter()

        final_result = sort_function(test_data)

        # Stop timing
        end = time.perf_counter()

        duration = end - start
        times.append(duration)

        # Verify sorting outside the measured time
        assert final_result == sorted(numbers)

        print(f"Run {run + 1}: {duration:.9f} seconds")

    average_time = sum(times) / len(times)

    print(f"Average time: {average_time:.9f} seconds")
    print("Sorting verified successfully.")

    return average_time, final_result


def python_timsort(numbers):
    """Sort using Python's built-in sorted() function."""

    return sorted(numbers)


def save_result(algorithm, size, average_time):
    """Append benchmark results to a CSV file."""

    results_folder = Path("results")
    results_folder.mkdir(exist_ok=True)

    csv_file = results_folder / "python_final_results.csv"

    file_exists = csv_file.exists()

    with open(csv_file, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(
                [
                    "algorithm",
                    "elements",
                    "average_time_seconds"
                ]
            )

        writer.writerow(
            [
                algorithm,
                size,
                f"{average_time:.9f}"
            ]
        )


def save_sorted_data(sorted_numbers):
    """Save sorted data to a text file."""

    results_folder = Path("results")
    results_folder.mkdir(exist_ok=True)

    output_file = results_folder / "sorted_output.txt"

    with open(output_file, "w") as file:

        for number in sorted_numbers:
            file.write(f"{number}\n")


def main():

    # Check that the user provided a data size
    if len(sys.argv) != 2:

        print(
            "Usage: python python_final_benchmark.py "
            "<number_of_elements>"
        )

        return

    # Convert terminal input into an integer
    try:
        limit = int(sys.argv[1])

    except ValueError:

        print(
            "Error: Number of elements must be an integer."
        )

        return

    # Reject invalid sizes
    if limit <= 0:

        print(
            "Error: Number of elements must be greater than 0."
        )

        return

    print(f"Numbers requested: {limit}")

    # Load data from CPUPI.txt
    numbers = load_numbers(
        "CPUPI.txt",
        limit
    )

    print(f"Numbers read: {len(numbers)}")

    # Check that enough numbers were available
    if len(numbers) != limit:

        print(
            "Error: CPUPI.txt does not contain "
            "the requested number of values."
        )

        return

    # -----------------------------------
    # Python Bubble Sort
    # -----------------------------------

    bubble_average, bubble_sorted = benchmark_sort(
        "Python Bubble Sort",
        bubble_sort,
        numbers
    )

    save_result(
        "Python Bubble Sort",
        len(numbers),
        bubble_average
    )

    # -----------------------------------
    # Python built-in Timsort
    # -----------------------------------

    timsort_average, timsort_sorted = benchmark_sort(
        "Python Timsort",
        python_timsort,
        numbers
    )

    save_result(
        "Python Timsort",
        len(numbers),
        timsort_average
    )

    # Both algorithms must give
    # exactly the same result
    assert bubble_sorted == timsort_sorted

    # Save the final sorted dataset
    save_sorted_data(timsort_sorted)

    print(
        "\nBoth algorithms produced "
        "the same sorted result."
    )

    print("Results saved to CSV.")

    print(
        "Sorted data saved to "
        "results/sorted_output.txt"
    )


if __name__ == "__main__":
    main()