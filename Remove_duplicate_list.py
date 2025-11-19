user_list = ['a','b','c','a','b','d','d','e']
new_list = []
# for i in user_list:
#   if i in new_list:
#     print("duplicate")
#   else:
#     new_list.append(i)
# print(new_list)


[new_list.append(x) for x in user_list if x not in new_list]
print(new_list)