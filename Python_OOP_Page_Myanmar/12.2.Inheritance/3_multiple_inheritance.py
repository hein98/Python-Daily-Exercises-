class Animal:
    def eat(self):
        print('Eating')

class Bird:
    def fly(self):
        print('Flying')

class BabyBird(Animal,Bird):
    def walk(self):
        print('Walking')
        
bb= BabyBird()
bb.walk()
bb.eat()
bb.fly()

# Walking
# Eating
# Flying