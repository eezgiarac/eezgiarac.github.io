
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

#define TEST_RUNS 1

// Bubble Sort: sort numbers in ascending order
void bubbleSort(long long array[], int size) {

    for (int step = 0; step < size - 1; ++step) {

        for (int i = 0; i < size - step - 1; ++i) {

            if (array[i] > array[i + 1]) {

                long long temp = array[i];
                array[i] = array[i + 1];
                array[i + 1] = temp;
            }
        }
    }
}

int main(int argc, char *argv[]) {

    // Check whether the user entered the number of elements
    if (argc != 2) {
        printf("Usage: %s <number_of_elements>\n", argv[0]);
        return 1;
    }

    // Convert the terminal argument from text to an integer
    int maxNumbers = atoi(argv[1]);

    if (maxNumbers <= 0) {
        printf("Error: Number of elements must be greater than 0.\n");
        return 1;
    }

    // Dynamically allocate memory
    long long *original =
        malloc((size_t)maxNumbers * sizeof(long long));

    long long *data =
        malloc((size_t)maxNumbers * sizeof(long long));

    if (original == NULL || data == NULL) {
        printf("Error: Memory allocation failed.\n");

        free(original);
        free(data);

        return 1;
    }

    // Open the dataset
    FILE *input = fopen("CPUPI.txt", "r");

    if (input == NULL) {
        printf("Error: Could not open CPUPI.txt\n");

        free(original);
        free(data);

        return 1;
    }

    int size = 0;

    // Read the requested number of values
    while (size < maxNumbers &&
           fscanf(input, "%lld", &original[size]) == 1) {

        size++;
    }

    fclose(input);

    if (size == 0) {
        printf("Error: No numbers were read.\n");

        free(original);
        free(data);

        return 1;
    }

    printf("Numbers requested: %d\n", maxNumbers);
    printf("Numbers read: %d\n\n", size);

    LARGE_INTEGER frequency;
    LARGE_INTEGER start;
    LARGE_INTEGER end;

    if (!QueryPerformanceFrequency(&frequency)) {
        printf("Error: High-resolution timer unavailable.\n");

        free(original);
        free(data);

        return 1;
    }

    double totalTime = 0.0;

    // Run the test five times
    for (int run = 0; run < TEST_RUNS; run++) {

        // Restore the original unsorted data
        for (int i = 0; i < size; i++) {
            data[i] = original[i];
        }

        // Start timing
        QueryPerformanceCounter(&start);

        bubbleSort(data, size);

        // Stop timing
        QueryPerformanceCounter(&end);

        double duration =
            (double)(end.QuadPart - start.QuadPart) /
            (double)frequency.QuadPart;

        totalTime += duration;

        printf("Run %d: %.9f seconds\n",
               run + 1, duration);

        // Verify that the data is correctly sorted
        for (int i = 1; i < size; i++) {

            if (data[i - 1] > data[i]) {

                printf("Error: Sorting verification failed.\n");

                free(original);
                free(data);

                return 1;
            }
        }
    }

    double averageTime = totalTime / TEST_RUNS;

    printf("\nAverage time: %.9f seconds\n",
           averageTime);

    // Save the result
    FILE *output =
        fopen("results/c_bubble_precise_results.csv", "a");

    if (output == NULL) {
        printf("Error: Could not open the CSV file.\n");

        free(original);
        free(data);

        return 1;
    }

    fseek(output, 0, SEEK_END);

    if (ftell(output) == 0) {
        fprintf(
            output,
            "algorithm,elements,average_time_seconds\n"
        );
    }

    fprintf(
        output,
        "C Bubble Sort,%d,%.9f\n",
        size,
        averageTime
    );

    fclose(output);

    // Release dynamically allocated memory
    free(original);
    free(data);

    printf("Sorting verified successfully.\n");
    printf("Precise result saved to CSV.\n");

    return 0;
}