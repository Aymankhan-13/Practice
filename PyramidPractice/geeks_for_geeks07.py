'''
A
B C
D E F
G H I J
K L M N O
'''

def alpha_pattern2(n):
    num = 65
    for i in range(n):
        for j in range(i+1):
            ch = chr(num)
            print(ch, end = ' ')
            num += 1
        print()


x = 5
alpha_pattern2(x)