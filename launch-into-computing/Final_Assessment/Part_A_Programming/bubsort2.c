

#include <stdio.h>
#include <time.h>

#define MAX_NUMBERS 5000
#define TEST_RUNS 5

// Sort numbers in ascending order
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

int main(void) {

    long long original[MAX_NUMBERS];
    long long data[MAX_NUMBERS];
    int size = 0;

    // Open the dataset
    FILE *file = fopen("CPUPI.txt", "r");

    if (file == NULL) {
        printf("Error: Could not open CPUPI.txt\n");
        return 1;
    }

    // Read the first 1000 numbers
    while (size < MAX_NUMBERS &&
           fscanf(file, "%lld", &original[size]) == 1) {
        size++;
    }

    fclose(file);

    if (size == 0) {
        printf("Error: No numbers were read.\n");
        return 1;
    }

    printf("Numbers read: %d\n\n", size);

    double totalTime = 0.0;

    // Repeat the sorting test five times
    for (int run = 0; run < TEST_RUNS; run++) {

        // Restore the original unsorted numbers
        for (int i = 0; i < size; i++) {
            data[i] = original[i];
        }

        // Measure only the sorting operation
        clock_t start = clock();

        bubbleSort(data, size);

        clock_t end = clock();

        double duration =
            (double)(end - start) / CLOCKS_PER_SEC;

        totalTime += duration;

        printf("Run %d: %.9f seconds\n",
               run + 1, duration);
    }

    double averageTime = totalTime / TEST_RUNS;

    printf("\nAverage time: %.9f seconds\n",
           averageTime);

    return 0;
}


