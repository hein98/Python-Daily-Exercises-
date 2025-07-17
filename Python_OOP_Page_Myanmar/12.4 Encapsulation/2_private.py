class Employee:
    __id=10
    
    def get_id(self): #getter
        print(self.__id,':  id inside class')
        
emp=Employee()
emp.get_id()
print(emp.__id)

#     print(emp.__id)
#           ^^^^^^^^
# AttributeError: 'Employee' object has no attribute '__id'