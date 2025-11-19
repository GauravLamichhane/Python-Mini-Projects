num = int(input("Enter the number upto you wanna print:"))

a,b = 0,1
while a <= num:
  print(a,end='\t')
  a , b = b , a+b