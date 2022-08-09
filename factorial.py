num=int(input("enter the number"))
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)
print("factorial of", num ," is",factorial(num))