from abc import ABC, abstractmethod


class Vehicle(ABC):  # Interface
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):  # Concrete class implementing the interface
    def drive(self):
        print("Car is moving")

    def stop(self):
        print("Car stopped")

car = Car()
car.drive()
car.stop()
