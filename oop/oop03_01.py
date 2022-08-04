# Class Methods: changing raise_amount
class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1    #

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount


emp_1 = Employee('Corey', 'Schafer', 60000)
emp_2 = Employee('Test', 'User', 50000)

print(emp_2.raise_amount)
Employee.set_raise_amt(1.05)        # replaces Employee.raise_amount = 1.05

print(emp_1.raise_amount)
print(emp_2.raise_amount)


