class Animal:
    def eat(self):
        print('Eating')
class Bird(Animal):
    def fly(self):
        print('Flying')
        
class BabyBird(Bird):
    def walk(self):
        print('Walking')
        
bb=BabyBird()
bb.eat()
bb.fly()
bb.walk()

# Eating
# Flying
# Walking