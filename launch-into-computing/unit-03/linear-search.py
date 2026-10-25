def linear_search(chargers, target_serial):
    for index, serial_number in enumerate(chargers):
        if serial_number == target_serial:
            return index

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
result = linear_search(charger_serials, target)

if result == -1:
    print("Charger not found.")
else:
    print("Charger found at index:", result)