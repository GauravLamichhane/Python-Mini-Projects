# print("Simple Calculator")

# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))

# if operator == '+':
#   result = num1 + num2
# elif operator == '-':
#   result = num1 - num2
# elif operator == '*':
#   result = num1 * num2
# elif operator == '/':
#   if num2 !=0:
#     result = num1 / num2
#   else:
#     print("Denominator should be > 1")
# else:
#   print("Enter a valid operator")

# print(f"Result:{result}")


#using function
def calculator(a,b,operator):
  def add(a,b): return a +b
  def sub(a,b): return a-b
  def mul(a,b): return a*b
  def div(a,b):
    if b!=0: 
      return a/b 
    else: return f"division by zero"

  operations = {
  '+':add,
  '-':sub,
  '*':mul,
  '/':div
}

  func = operations.get(operator)
  if func:
    return func(a,b)
  else:
    return "Invalid operator!"
  
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

result = calculator(num1, num2, operator)
print(f"Result: {result}")
