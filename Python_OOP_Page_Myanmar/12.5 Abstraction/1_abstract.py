#ABC= Abstract Base Class

from abc import ABC,abstractmethod

class Bird(ABC):
    def eat(self):
        print('Eating')
        
    @abstractmethod 
    def fly(self):
        pass

class Eagle(Bird):
    def eat(self):
        print('Eating Eagle')
        
    def fly(self):
        print('Flying Eagle')
        
eagle=Eagle()
eagle.eat()
eagle.fly()