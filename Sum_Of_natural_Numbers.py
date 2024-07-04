
#Sum Of Natural Numbers Using Function
'''def sum(n):
    sum = 0
    for i in range(n):
        sum = sum + (i+1)
        i=i+1
    
    return sum

n = int(input("Enter a Number:\n"))
print(sum(n))'''


#Sum Of Natural Numbers Using Recursion
def sum_recursion(n):
    if n==0 :
       return 0
    else :
        return (sum_recursion(n-1) + int(n))

n = int(input("Enter Any Natural Number:\n"))
print(sum_recursion(n))
