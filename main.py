print("Factorial of a number".center(60,'#'))
n= int(input("Enter a number"))
if n < 0:
   print("The factorial of {0}is 0". format (n))
elif n == 0 or n == 1:
   print("The factorial of {0}is 1".format(n))
else:
   fact = 1
   for i in range(1,n+1):
    fact = fact * i
    print("The factorial of{0} is{1}".format(n,fact))
   