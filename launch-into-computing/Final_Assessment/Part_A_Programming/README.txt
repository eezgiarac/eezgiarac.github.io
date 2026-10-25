PART A — FINAL SUBMISSION PACKAGE | 15 October 2026
Evaluating the Development Models of Python and C

START HERE
Part_A_Final_Report.docx — final report with Table 1 under section 4 (Results).
CPUPI.txt — tutor-provided input dataset (838,861 numeric values).
sorted_output_all_838861.txt — ascending numerical output for all 838,861 values.

SOURCE CODE
bubsort_original.py / bubsort2_original.c — preserved tutor starting code.
bubsort.py — edited Python bubble sort reading CPUPI.txt; demonstration limited to 1,000 values.
bubsort2.c — edited C bubble sort reading 5,000 values; five-run functional test.
python_timsort_final.py — efficient Python built-in sorted() benchmark, five repetitions.
python_final_benchmark.py — additional Python benchmark including 1,000-element bubble sort.
c_performance_precise.c — Windows-specific C bubble-sort benchmark for requested dataset sizes; one timed run per recorded size.
generate_full_sorted_output.py — independently creates and validates the complete ascending output; not part of the historical timed tests.

RECORDED EVIDENCE
c_bubble_precise_results.csv — historical C timings, including 100,000 and 200,000 elements.
python_timsort_final_results.csv — historical Python sorted() timings at 100,000, 200,000, 500,000, 800,000 elements.
python_final_results.csv — additional Python timings, including the small bubble-sort baseline.
The report contains the consolidated results table. Other recorded CSV rows must not be interpreted as missing measurements for the required comparison.

REPRODUCTION (Windows, from the extracted folder containing CPUPI.txt)
Python 3.12 or compatible:
  python generate_full_sorted_output.py
  python bubsort.py
  python python_timsort_final.py 100000
  python python_timsort_final.py 200000
  python python_timsort_final.py 500000
  python python_timsort_final.py 800000
  python python_final_benchmark.py 1000
GCC (MSYS2 MinGW, example):
  gcc -O2 -o bubble_check.exe bubsort2.c
  ./bubble_check.exe
  gcc -O2 -o c_bubble.exe c_performance_precise.c
  ./c_bubble.exe 100000
  ./c_bubble.exe 200000
CAUTION: 500,000 and 800,000 C bubble-sort runs may take a very long time. These commands reproduce methods, not necessarily exact historical timings. Windows-specific code uses QueryPerformanceCounter.

MEASUREMENT LIMITATIONS
Python bubble-sort timings at 100k/200k/500k/800k: not measured.
C bubble-sort timings at 500k/800k: not measured.
Historical large-input C results are single runs; Python sorted() results are five-run averages. The GCC 16.2.0 installation verified later must not be attributed to historical runs. Missing values have not been estimated or fabricated.

ACADEMIC INTEGRITY
The full sorted output was generated separately after historical timing runs. Please review all content, confirm your understanding, and make any AI-use declaration required by your university. The report documents methodological limitations.
