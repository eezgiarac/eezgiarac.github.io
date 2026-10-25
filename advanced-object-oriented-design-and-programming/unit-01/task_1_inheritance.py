"""Unit 1, Task 1: Basic class hierarchy (inheritance)."""


class Vehicle:
    def __init__(self, brand, fuel_type):
        self.brand = brand
        self.fuel_type = fuel_type


class Car(Vehicle):
    def __init__(self, brand, fuel_type, num_doors):
        super().__init__(brand, fuel_type)
        self.num_doors = num_doors


if __name__ == "__main__":
    car = Car("Tesla", "Electric", 4)
    print(f"Brand: {car.brand}")
    print(f"Fuel type: {car.fuel_type}")
    print(f"Number of doors: {car.num_doors}")
