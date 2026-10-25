"""Unit 1, Task 4: Abstract animal class and implementations."""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


if __name__ == "__main__":
    animals = [Dog(), Cat()]
    for animal in animals:
        print(f"{type(animal).__name__}: {animal.make_sound()}")
