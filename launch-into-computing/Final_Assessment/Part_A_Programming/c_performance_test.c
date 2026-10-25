
#include <stdio.h>
#include <time.h>

#define MAX_NUMBERS 10000
#define TEST_RUNS 5

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

    FILE *input = fopen("CPUPI.txt", "r");

    if (input == NULL) {
        printf("Error: Could not open CPUPI.txt\n");
        return 1;
    }

    while (size < MAX_NUMBERS &&
           fscanf(input, "%lld", &original[size]) == 1) {
        size++;
    }

    fclose(input);

    if (size == 0) {
        printf("Error: No numbers were read.\n");
        return 1;
    }

    double totalTime = 0.0;

    for (int run = 0; run < TEST_RUNS; run++) {

        // Copy the original unsorted numbers
        for (int i = 0; i < size; i++) {
            data[i] = original[i];
        }

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

    printf("Average time: %.9f seconds\n",
           averageTime);

    // Append the result to the CSV file
    FILE *output = fopen("results/c_bubble_results.csv", "a");

    if (output == NULL) {
        printf("Error: Could not open the results file.\n");
        return 1;
    }

    fprintf(output, "C Bubble Sort,%d,%.9f\n",
            size, averageTime);

    fclose(output);

    printf("Result saved to CSV.\n");

    return 0;
}
