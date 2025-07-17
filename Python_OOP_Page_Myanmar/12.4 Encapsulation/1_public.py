class Employee:
    id =10
    
    def get_id(self):
        print('id inside class => ',self.id)
        
emp=Employee()
emp.get_id()
print('id outside class =>',emp.id)

# id inside class =>  10
# id outside class => 10