class Animal:
    def eat(self):
        print('Eating')
 
class Bird(Animal):       
    def fly(self):
        print('Flying')
        
bird=Bird()
bird.eat()
bird.fly()