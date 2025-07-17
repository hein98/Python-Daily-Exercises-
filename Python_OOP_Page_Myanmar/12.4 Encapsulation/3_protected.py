class ParentEmployee:
    _id=10
    
class Employee(ParentEmployee):
    def get_id(self):
        print('id inside class: ',self._id)
        
emp=Employee()
emp.get_id()
print('ID Outside Class: ',emp._id)

# id inside class:  10
# ID Outside Class:  10