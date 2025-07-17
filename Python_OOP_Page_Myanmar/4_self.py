class Bird:
    size=10
    name='crow'
    color='black'
    food='rice'
    
    def eat(self):
        print(f'{self.name} is eating {self.food}')
        
b=Bird()
b.eat()

# crow is eating rice