from abc import ABC,abstractmethod

class Bird(ABC):
    def eat(self):
        print('Eating')
        
    @abstractmethod
    def fly(self):
        pass
    
class Eagle(Bird):
    def eat(self):
        print('Eagle Eating')
        
eagle=Eagle()
eagle.fly()

# TypeError: Can't instantiate abstract class Eagle with abstract method fly