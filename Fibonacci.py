#Print Fibonacci Sequence
def fibonacci(n):
   # first two terms
   n1, n2 = 0, 1
   count = 1

   # check if the number of terms is valid
   if n <= 0:
       print("Please enter a positive integer")
   # if there is only one term, return n1
   elif n == 1:
      print("Fibonacci sequence upto",n,":")
      print(n1)
   # generate fibonacci sequence
   else:
      print("Fibonacci sequence:")
      while count < n:
         print(n1)
         nth = n1 + n2
         # update values
         n1 = n2
         n2 = nth
         count += 1
         

#SUM of Fibonacci Terms
def fibonacci_sum(n):
   if n<=1:
        return n
   else :
      return fibonacci_sum(n-1) + fibonacci_sum(n-2)
   print(n)





n = int(input("Enter Num Of Terms Req:\n"))
print(fibonacci(n))
print("The Nth Term Is:",fibonacci_sum(n))
