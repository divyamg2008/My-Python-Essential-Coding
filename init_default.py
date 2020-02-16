class employee:
    def __init__(self, **kwargs):
        self._id = kwargs['ID'] if 'ID' in kwargs else '0000'
        self._name = kwargs['name'] if 'name' in kwargs else 'xyz'
        self._age = kwargs['age'] if 'age' in kwargs else 'XX'

    def employee_details(self):
        return (f"ID: {self._id} name: {self._name} age: {self._age}")

    # getter and setter
    def age(self, a=None):
        if a:
            self._age = a
        return self._age

    def __str__(self):
        return(f"ID -> {self._id} name-> {self._name} age-> {self._age}")


new = employee()
print(new.employee_details())

divya = employee(name='divya', age='32', ID='2124')
print(divya.employee_details())
divya = employee(name='divya', ID='2124')
print(divya.employee_details())
divya.age(45)
print(divya.employee_details())
print(divya.__str__())
