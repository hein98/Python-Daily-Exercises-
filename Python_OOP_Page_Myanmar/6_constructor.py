class Bird:
    def __init__(self,name,color,size,food):
        self.name=name
        self.color=color
        self.size=size
        self.food=food
        
    def eat(self):
        print(f'{self.name} will eat {self.food}')
        
crow=Bird('crow','black',10,'rice')
crow.eat()
# crow will eat rice

Eagle=Bird('eagle','brown and white',15,'flash')
Eagle.eat()
# eagle will eat flash