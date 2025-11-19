list = ['apple','banana','mango','kiwi']
"""

#without
new_list = []
for item in list:
  if "a" in item:
    new_list.append(item)
print(new_list)

"""
#with comprehension

"""
1. for x in list
loop through each item on list
on first iter x = apple , 2nd x = banana
2. if "a" in x
return true if a exists else false
3.x at the start if the cond is true add x to the new list
"""
new_list = [x for x in list if "a" in x]
print(new_list)