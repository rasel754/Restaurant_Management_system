from abc import ABC

class User(ABC) : 
    def __init__(self, name , phone , email , address):
        self.name=name
        self.email=email
        self.address=address
        self.phone=phone


class Employee(User):
    def __init__(self, name, phone, email, address , age , salary, designation):
        super().__init__(name, phone, email, address)
        self.age=age
        self.salary=salary
        self.designation =designation


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.employees=[] #it's our data base
    
    def add_employee(self , name , email , phone , address,age , salary, designation):
        #create an objet of employee class
        employee=Employee(name , email , address , phone,age , salary, designation)
        self.employees.append(employee)
        print(f"{name} is added as a new employee..")

    def view_employee(self):
        print("Employee List :-")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone , emp.address)
    