# num = [1,2,3,4,5,6]
# print(num)
# print(*num)#unpacking operator prints the number individually


def pizza(size,*toppings,**delivery):#*args and **kwargs can be named as anything
  print(f"The size of the pizza is:{size} and the toppings are :{toppings}")
  print(f"The delivery options are :{delivery}")

pizza("Large","Peporoni","Chilli","Olive oil",online = True , tip = 5)