import sys
import time
import csv
from pathlib import Path


TEST_RUNS = 5


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


def main():

    if len(sys.argv) != 2:
        print(
            "Usage: python python_timsort_final.py "
            "<number_of_elements>"
        )
        return

    try:
        limit = int(sys.argv[1])

    except ValueError:
        print("Error: Number of elements must be an integer.")
        return

    if limit <= 0:
        print("Error: Number of elements must be greater than 0.")
        return

    print(f"Numbers requested: {limit}")

    numbers = load_numbers("CPUPI.txt", limit)

    print(f"Numbers read: {len(numbers)}")

    if len(numbers) != limit:
        print(
            "Error: CPUPI.txt does not contain "
            "the requested number of values."
        )
        return

    times = []
    final_result = None

    print("\nPython Timsort")
    print("-" * 40)

    for run in range(TEST_RUNS):

        test_data = numbers.copy()

        # Only the sorting operation is timed
        start = time.perf_counter()

        final_result = sorted(test_data)

        end = time.perf_counter()

        duration = end - start
        times.append(duration)

        # Verification is outside the measured time
        assert final_result == sorted(numbers)

        print(
            f"Run {run + 1}: "
            f"{duration:.9f} seconds"
        )

    average_time = sum(times) / len(times)

    print(
        f"\nAverage time: "
        f"{average_time:.9f} seconds"
    )

    print("Sorting verified successfully.")

    # Create results folder if necessary
    results_folder = Path("results")
    results_folder.mkdir(exist_ok=True)

    # Save timing result
    csv_file = (
            results_folder /
            "python_timsort_final_results.csv"
    )

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
                "Python Timsort",
                len(numbers),
                f"{average_time:.9f}"
            ]
        )

    # Save sorted data
    sorted_file = (
            results_folder /
            "sorted_output.txt"
    )

    with open(sorted_file, "w") as file:

        for number in final_result:
            file.write(f"{number}\n")

    print("Result saved to CSV.")
    print(
        "Sorted data saved to "
        "results/sorted_output.txt"
    )


if __name__ == "__main__":
    main()