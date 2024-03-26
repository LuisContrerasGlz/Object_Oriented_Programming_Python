class Person:
    def __init__(self, name, age):
        self._name = name        # Protected attribute
        self._age = age          # Protected attribute

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            print("Age cannot be negative.")

# Creating an instance of the Person class
person = Person("Alice", 30)

# Accessing attributes using property decorators
print("Name:", person.name)
print("Age:", person.age)

# Updating attributes using property decorators
person.name = "Bob"
person.age = 25

# Accessing updated attributes
print("Updated Name:", person.name)
print("Updated Age:", person.age)

# Trying to set negative age
person.age = -10  # This will print "Age cannot be negative."
