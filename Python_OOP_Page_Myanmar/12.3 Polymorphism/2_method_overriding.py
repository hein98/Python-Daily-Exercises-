class Bird:
    def fly(self):
        return 100
    
class Eagle(Bird):
    def fly(self):
        return 1000
    
class Crow(Bird):
    def fly(self):
        return 500
    
bird=Bird()
eagle=Eagle()
crow=Crow()

eagle.fly()
crow.fly()

print('Bird flying %d Meter Height'%(bird.fly()))
print('Eagle flying %d Meter Height'%(eagle.fly()))
print('Crow flying %d Meter Height'%(crow.fly()))