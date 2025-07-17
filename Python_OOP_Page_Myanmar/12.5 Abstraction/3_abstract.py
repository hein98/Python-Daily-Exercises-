from abc import ABC,abstractmethod

class Bird(ABC):
    def eat(self):
        print('Eating')
        
    @abstractmethod
    def fly(self):
        pass
    
bird=Bird()
bird.fly()