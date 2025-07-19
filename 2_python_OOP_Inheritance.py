class Animal:
    def __init__(self,name):
        self.name=name
        
    def walk(self):
        print(f'{self.name} walks!')
        
    def eat(self):
        print(f'{self.name} eats!')

class Dog(Animal):
    pass 

class Cat(Animal):
    pass

new_dog=Dog('Larry')
new_dog.walk() #Functions inherited from the class Animal
new_dog.eat()

new_cat=Cat('Luna')
new_cat.walk() #Functions inherited from the class Animal
new_cat.eat()

