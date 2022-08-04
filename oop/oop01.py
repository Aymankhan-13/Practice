class Employee:
    def __init__(self, first, last, pay):    #Constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):                     #the instance is getting passed as an argument, eg emp_1
       return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)


#print(emp_1)  # instance variable contains data that is unique to each instance.
#print(emp_2)


'''
emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000

__init__ used above
'''

print(emp_1.email)
print(emp_2.email)
print(Employee.fullname(emp_1))
print(emp_2.fullname())

'''
print('{} {}'.format(emp_1.first, emp_1.last))
function defined above
'''