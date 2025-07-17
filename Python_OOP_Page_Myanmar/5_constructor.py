class Bird:
    name='Crow'
    size=10
    color='black'
    food='rice'
    
    def eat(self):
        print(f'{self.name} is eating {self.food}')
    
b=Bird()
b.eat()
eagle=Bird()
eagle.eat()

# Crow is eating rice
# Crow is eating  rice // wrong