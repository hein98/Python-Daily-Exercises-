class Animal:
    def eat(self):
        print('Eating')
        
class Bird(Animal):
    def fly(self):
        print('Flying')
        
eagle=Bird()
print(isinstance(eagle,Bird))

# True