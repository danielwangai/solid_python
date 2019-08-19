"""
Classes are open for extension but closed for modification.
"""

class Employee:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def salary(self):
        pass



employees = [
    Employee("Dan"),
    Employee("Dave"),
    Employee("Kim"),
]

def get_salaries(emloyees):
    for employee in employees:
        if employee.name == "Dan":
            print(150000)
        if employee.name == "Dave":
            print(30000)
        if employee.name == "Kim":
            print(50000)

"""
If we are to add a new employee, say Jane, we'll have to modify
the get_salaries function to include the new employee's salary.
"""

get_salaries(employees)


class Manager(Employee):
    def annual_salary(self):
        return 150000


class Janitor(Employee):
    def annual_salary(self):
        return 30000


class Secretary(Employee):
    def annual_salary(self):
        return 50000


"""
print_salaries function will not be modified when we add a new employee.
"""
def print_salaries(employees):
    if not employees:
        print("No emloyees")
        return
    for i in employees:
        print(i.annual_salary())


employees_2 = [
    Manager("Dan"),
    Janitor("Dave"),
    Secretary("Kim"),
]
print("\n")
print_salaries(employees_2)
