"""Unit 1, Task 5: Constructor and destructor.

Note: __del__ timing is implementation-dependent; it is not suitable
for guaranteed cleanup of external resources.
"""


class Person:
    def __init__(self, name):
        self.name = name
        print(f"Hello, {self.name}!")

    def __del__(self):
        print(f"Goodbye, {self.name}!")


if __name__ == "__main__":
    person = Person("Alex")
    del person
