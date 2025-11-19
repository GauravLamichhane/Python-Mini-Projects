#syntax => lambda arguements: expression
# x = lambda a : a+10
# print(x(5))

# x = lambda a,b: a*b
# print(x(5,10))

def myfunc(n):
  return lambda a: a* n

doubler = myfunc(2)
print(doubler(11))