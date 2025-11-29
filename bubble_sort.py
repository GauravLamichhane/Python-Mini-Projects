


# def bubble_sort(arr):
#   for i in range(len(arr)):
#     for j in range(i):
#       if j[j] > j[j+1]:
#         temp = 


# print(len(arr))
# bubble_sort(arr)
def bubble_sort(arr):
  for i in range(len(arr)-1):#after n-1 passes the list is automatically sorted
    for j in range(len(arr) - i-1):
      if arr[j]>arr[j+1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
  return arr

arr = [9,1,8,2,7,3,6,4,5]
print("Sorted Array")
print(bubble_sort(arr))
