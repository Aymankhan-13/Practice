# Property Decorators
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property       # Allows methods to be accessed as attributes
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Name deleted.')
        self.first = None
        self.last = None


'''
emp_1 = Employee('John', 'Smith')
emp_1.first = 'Jim'  --> here the  email does not get updated
'''

emp_1 = Employee('John', 'Smith')
print(emp_1.fullname)

emp_1.fullname = 'Corey Schafer'
print(emp_1.fullname)

del emp_1.fullname

