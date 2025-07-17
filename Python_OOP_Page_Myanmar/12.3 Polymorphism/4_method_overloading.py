# Method OVERLOADING:  Having multiple method with the same name but different parameters
class Animal:
    def speak(self):
        print('speaking')#it gets overridden in the Dog class.


class Dog(Animal):
    def speak(self,word=None,time=2):
        if word == None:
            print('Barking')
            
        else:
            print(word*time)
            
d=Dog()
d.speak()
d.speak('woof')
d.speak('woof',3)


# Barking
# woofwoof
# woofwoofwoof