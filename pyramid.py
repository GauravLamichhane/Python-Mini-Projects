# rows = int(input("Enter the level up to which you want to print: "))

# for i in range(5):
#   for j in range(i+1):
#     print("*",end ="")
#   print()
# for i in range(rows):
#   for j in range(rows):
#     rows = rows - 1
#     print("*",end="")
#   print()

# for j in range(1):
#   print("*")
# rows = 5
# for i in range(rows):
#   for j in range(rows-i):
#     print("*",end = "")
     
#   print()
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2*i - 1))