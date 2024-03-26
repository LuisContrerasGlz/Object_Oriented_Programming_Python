class Person:
    def __init__(self, name, age):
        self._name = name        # Protected attribute
        self._age = age          # Protected attribute

    # Getter method for name
    def get_name(self):
        return self._name

    # Setter method for name
    def set_name(self, name):
        self._name = name

    # Getter method for age
    def get_age(self):
        return self._age

    # Setter method for age
    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Age cannot be negative.")

# Creating an instance of the Person class
person = Person("Alice", 30)

# Accessing attributes using getter methods
print("Name:", person.get_name())
print("Age:", person.get_age())

# Updating attributes using setter methods
person.set_name("Bob")
person.set_age(25)

# Accessing updated attributes
print("Updated Name:", person.get_name())
print("Updated Age:", person.get_age())

# Trying to set negative age
person.set_age(-10)  # This will print "Age cannot be negative."
