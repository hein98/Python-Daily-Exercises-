class Employee:
    __id=10
    
    def change_id(self,id): #setter
        if id>20:
            print('Id greater than 20 is not allowed to set.')
        else:
            self.__id= id
            print('Id Inside Class is changed to =>',self.__id)

    def get_id(self): #getter
        print(self.__id)
        
emp=Employee()

emp.get_id()
emp.change_id(5)
emp.change_id(25)

# 10
# Id Inside Class is changed to =>5
# Id greater than 20 is not allowed to set.