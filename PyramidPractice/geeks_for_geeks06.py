'''
A
B B
C C C
D D D D
E E E E E
'''
def alpha_pattern(n):
    num = 65
    for i in range(n):
        for j in range(i+1):
            ch = chr(num)
            print(ch, end = ' ')
        num += 1
        print()


x = 5
alpha_pattern(x)