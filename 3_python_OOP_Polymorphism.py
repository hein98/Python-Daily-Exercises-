

class French:
    def say_hello(self):
        print('Bonjour')
        
class Thai:
    def say_hello(self): #method overriding 
        print('Swadee Krap')
        
class Chinese:
    def say_hello(self):
        print('Ni Hao')
        
def introduction(x): #duck typing
    print (x.say_hello())
    
Mary=French()
Joon=Thai()
Kiwi=Chinese()

Kiwi.say_hello()
# -----------------------------------------------------

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):  # Overrides Animal.speak()
        return "Woof!"

dog = Dog()
print(dog.speak())  # Output: "Woof!" (from Dog, not Animal)