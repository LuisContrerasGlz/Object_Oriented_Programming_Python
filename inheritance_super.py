class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name} from Parent class."


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calling the Parent class constructor
        self.age = age

    def greet(self):
        parent_greeting = super().greet()  # Calling the greet() method from the Parent class
        return f"{parent_greeting} I am {self.age} years old."


# Creating an instance of the Child class
child = Child("Alice", 10)

# Calling the greet() method of the Child class
print(child.greet())
