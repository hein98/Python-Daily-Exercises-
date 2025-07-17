from abc import ABC,abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def drive(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
class Car(Vehicle):
    def drive(self):
        return 'You drive the car'
    def stop(self):
        return 'You stop the car'
    
    
class Boat(Vehicle):
    def drive(self):
        print('You drive the boat')
    def stop(self):
        print('You anchor the boat')
car=Car()
print(car.drive())
print(car.stop())

boat=Boat()
boat.drive()
boat.stop()