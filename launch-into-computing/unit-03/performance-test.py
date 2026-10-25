import csv
import time


def linear_search(data, target):
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1


def binary_search(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        middle = (left + right) // 2

        if data[middle] == target:
            return middle
        elif data[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def measure_time(search_function, data, target, repetitions):
    start_time = time.perf_counter()

    for _ in range(repetitions):
        search_function(data, target)

    end_time = time.perf_counter()

    average_seconds = (end_time - start_time) / repetitions
    return average_seconds * 1000


input_sizes = [100, 1000, 10000, 100000]
results = []

for size in input_sizes:
    test_data = list(range(size))
    target = size - 1

    if size <= 1000:
        repetitions = 1000
    elif size <= 10000:
        repetitions = 500
    else:
        repetitions = 100

    linear_time = measure_time(
        linear_search, test_data, target, repetitions
    )

    binary_time = measure_time(
        binary_search, test_data, target, repetitions
    )

    results.append([size, linear_time, binary_time])

    print(
        f"Input size: {size}, "
        f"Linear Search: {linear_time:.6f} ms, "
        f"Binary Search: {binary_time:.6f} ms"
    )


with open(
        "performance-results.csv",
        "w",
        newline="",
        encoding="utf-8"
) as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([
        "Input Size",
        "Linear Search Time (ms)",
        "Binary Search Time (ms)"
    ])
    writer.writerows(results)


width = 900
height = 550
margin_left = 90
margin_right = 40
margin_top = 60
margin_bottom = 80

plot_width = width - margin_left - margin_right
plot_height = height - margin_top - margin_bottom

maximum_time = max(row[1] for row in results)

points_linear = []
points_binary = []

for position, row in enumerate(results):
    x = margin_left + position * (
            plot_width / (len(results) - 1)
    )

    linear_y = (
            margin_top
            + plot_height
            - (row[1] / maximum_time) * plot_height
    )

    binary_y = (
            margin_top
            + plot_height
            - (row[2] / maximum_time) * plot_height
    )

    points_linear.append(f"{x},{linear_y}")
    points_binary.append(f"{x},{binary_y}")


svg_lines = [
    f'<svg xmlns="http://www.w3.org/2000/svg" '
    f'width="{width}" height="{height}">',
    '<rect width="100%" height="100%" fill="white"/>',
    '<text x="450" y="30" text-anchor="middle" '
    'font-size="22">Search Algorithm Performance</text>',
    f'<line x1="{margin_left}" y1="{margin_top}" '
    f'x2="{margin_left}" y2="{margin_top + plot_height}" '
    'stroke="black"/>',
    f'<line x1="{margin_left}" y1="{margin_top + plot_height}" '
    f'x2="{margin_left + plot_width}" '
    f'y2="{margin_top + plot_height}" stroke="black"/>',
    f'<polyline points="{" ".join(points_linear)}" '
    'fill="none" stroke="#d62728" stroke-width="3"/>',
    f'<polyline points="{" ".join(points_binary)}" '
    'fill="none" stroke="#1f77b4" stroke-width="3"/>',
]

for position, row in enumerate(results):
    x = margin_left + position * (
            plot_width / (len(results) - 1)
    )

    svg_lines.append(
        f'<text x="{x}" y="{margin_top + plot_height + 25}" '
        f'text-anchor="middle" font-size="13">{row[0]}</text>'
    )

svg_lines.extend([
    '<text x="450" y="530" text-anchor="middle" '
    'font-size="16">Input Size</text>',
    '<text x="20" y="275" text-anchor="middle" '
    'font-size="16" transform="rotate(-90 20 275)">'
    'Average Execution Time (ms)</text>',
    '<line x1="590" y1="55" x2="625" y2="55" '
    'stroke="#d62728" stroke-width="3"/>',
    '<text x="635" y="60" font-size="14">Linear Search</text>',
    '<line x1="590" y1="80" x2="625" y2="80" '
    'stroke="#1f77b4" stroke-width="3"/>',
    '<text x="635" y="85" font-size="14">Binary Search</text>',
    '</svg>'
])

with open(
        "performance-comparison.svg",
        "w",
        encoding="utf-8"
) as svg_file:
    svg_file.write("\n".join(svg_lines))


print("\nFiles created:")
print("performance-results.csv")
print("performance-comparison.svg")