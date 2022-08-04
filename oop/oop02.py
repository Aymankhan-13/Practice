class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1    # Employee. doesn't let instance change value

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  #can use self. or Employee. >> self. lets instance change value


print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 60000)
emp_2 = Employee('Test', 'User', 50000)

print(Employee.num_of_emps)

print(emp_1.__dict__)      # Class Employee contains raise_amount attribute used by instances
print(Employee.__dict__)

'''
Employee.raise_amount = 1.05  >> changes raise_amount for class and instances 
emp_1.raise_amount = 1.05  >> changes raise_amount for that particular instance 
'''

