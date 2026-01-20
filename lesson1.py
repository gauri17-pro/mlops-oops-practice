# Define a class 
class Employee:
    # Special function/ magic method/dunder method
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "Software Engineer"


    def work(self, department):
        print("Employee is working in the", department, "department")

# Create an object/instance of the class
emp1 = Employee()

print(emp1.salary)  # Accessing the salary attribute of the emp1 object

emp1.work("Finance")
print(type(emp1))  # Output: <class '__main__.Employee'>