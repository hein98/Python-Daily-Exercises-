class Animal:
    def eat(self):
        print('Eating')
        
class Bird(Animal):
    def fly(self):
        print('Flying')
        
print(issubclass(Animal,Bird))
print(issubclass(Bird,Animal))

# False
# True