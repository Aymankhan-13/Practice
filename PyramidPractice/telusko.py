'''                         https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/
# # # #
# # # #
# # # #
# # # #
'''

for i in range(4):
    for j in range(4):
        print('# ', end = '')
    print()

print('\n\n')

'''
#
# #
# # #
# # # #
'''

for i in range(4):
    for j in range(i+1):
        print('# ', end = '')
    print()

print('\n\n')

'''
# # # #
# # # 
# # 
# 
'''

for i in range(4):
    for j in range(4-i):
        print('# ', end = '')
    print()

