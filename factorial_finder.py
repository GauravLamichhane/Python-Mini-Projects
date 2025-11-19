print("Factorial Finder")
num = int(input("Enter the number: "))

# def factorial(n):
#   if n == 0 or n == 1:
#     return 1
#   return n *factorial(n-1)

# fact = factorial(n = num)
# print(fact)



def factorial_iterative(n):
  if n<0:
    print("Enter a positive number")
  elif n == 0:
    return 1
  else:
    fact = 1
    for i in range(1,n+1):
      fact = fact * i
    return fact

num = 5
print(f'The factorial is {factorial_iterative(n = num)}')