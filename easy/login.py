import time

user_name = 'ayman'
pwd = 'secretpwd'

name_input = input('Username: ')
pwd_input = input('Password: ')

if name_input == user_name and pwd_input == pwd:
    print('Access granted.')
    print('Please wait')
    time.sleep(5)
    print('Loading..')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    print('Alright you have security clearance. Pulling up the secret mainframe.')
elif name_input == user_name and pwd_input != pwd:
    print('Password incorrect.')
elif user_name != user_name and pwd_input != pwd:
    print('Username incorrect. ')
else:
    print('Check both fields.')
