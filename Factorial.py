
#Factorial By Using RECURSION 
def funct_recursion(n):
    if n==1 or n==0 :
        return 1
    else :
        return funct_recursion(n-1) * n

n = int(input("Enter a Number:\n"))
print(funct_recursion(n))





#Factorial By Using FUNCTION
'''def factorial(n):
    fact = 1
    for i in range(n):
        fact = fact * (i+1)
        i=i+1
    
    return fact

n = int(input("Enter a Number:\n"))
print(factorial(n))'''