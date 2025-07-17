class Bird:
    def fly(self): #parent method
        print('Bird Flying')
        
class Eagle(Bird):
    def fly(self): #child overrides the method
        print('Eagle Flying')
        
eagle=Eagle()
eagle.fly()

# Method overriding is when a child class provides its own version of a method that is already defined in its parent class.