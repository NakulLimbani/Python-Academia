#Star Pattern increasing
'''num = int(input("Enter num of Rows:\n"))
for i in range(num):
    print("*" * (i+1))
'''



#Star Pattern Decreasing
'''n = int(input("Enter Number Of Rows:\n"))
for i in range(n):
    print("*" * (n-i))'''

       #OR

'''n = int(input("Enter Number Of Rows:\n"))
i=0
for i in range(n,i,-1):
    print("*" * (i))'''


#Pyramid Star pattern
'''num = int(input("Enter num of Rows:\n"))
for i in range(num):
    print(" " * (num-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (num-i-1))'''




#Hollow Square Pattern
'''side = int(input("Please Enter any Side of a Square  : "))
for i in range(side):
    for j in range(side):
        if(i == 0 or i == side - 1 or j == 0 or j == side - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()'''




#Print {N}Pattern Using Star
'''side = int(input("Please Enter any Side of a Square  : "))
for j in range(side):
    for i in range(side):
        if  (i==j or i== 0 or i == side - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()'''




#Print {Z} pattern Using Stars
side = int(input("Please Enter any Side of a Square  : "))
for i in range(side):
    for j in range(side):
        if  (i == 0 or i == side-1 or i+j == side-1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()







