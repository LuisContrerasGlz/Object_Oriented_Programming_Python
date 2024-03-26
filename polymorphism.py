# Compile-time Polymorphism (Method Overloading):

class MathOperations:
    # Method with default parameter
    def add(self, a, b=0):  
        return a + b

math = MathOperations()
print(math.add(5))    # Outputs: 5 (5 + 0)
print(math.add(2, 3))  # Outputs: 5 (2 + 3)

# Runtime Polymorphism (Method Overriding):

class Animal:
    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.make_sound())

