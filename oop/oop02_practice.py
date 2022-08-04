class Employee:
    raise_amt = 1.04
    no_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def raise_pay(self):
        self.pay = self.pay * self.raise_amt


emp_1 = Employee('John', 'McClain', 60000)
emp_2 = Employee('Kyle', 'Reeves', 50000)

print(emp_1.__dict__)
emp_1.raise_amt = 1.05
print(emp_1.__dict__)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print('\n')
print(Employee.no_of_emps)



