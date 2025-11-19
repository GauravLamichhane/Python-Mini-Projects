# with open('gaurav.txt','w') as file:
#   file.write("internnnnnnn")
#   file.write("whastttt")
# print("File written succesfullly")



#reading from the file

# f = open('gaurav.txt','r')
# print('filename:',f.name)
# print('mode:',f.mode)
# print("Is closed:",f.closed)
# f.close()
# print("Is closed:",f.closed)


# file = open('gaurav.txt','r')
# content = file.read()
# print(content[5])

# with open('gaurav.txt','w') as f:
#   f.write("This is the first line.\n")
#   f.write("This is the second line.\n")
#   f.write("This is the third line.\n")
#   f.write("This is the fourth line.\n")
#   f.write("This is the fifth line.\n")
content  = open('gaurav.txt','r')
# print(content.read())

def print_n_lines(n):
  for i in range(0,n):
    print(content.readline())

print_n_lines(3)



