def binary_search(chargers, target_serial):
    left = 0
    right = len(chargers) - 1

    while left <= right:
        middle = (left + right) // 2

        if chargers[middle] == target_serial:
            return middle
        elif chargers[middle] < target_serial:
            left = middle + 1
        else:
            right = middle - 1

    return -1


charger_serials = [
    "EV-CHG-1001",
    "EV-CHG-1002",
    "EV-CHG-1003",
    "EV-CHG-1004",
    "EV-CHG-1005",
    "EV-CHG-1006"
]

target = "EV-CHG-1005"
result = binary_search(charger_serials, target)

if result == -1:
    print("Charger not found.")
else:
    print("Charger found at index:", result)