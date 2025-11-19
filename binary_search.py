#To implement the bonary search the array must be sorted
def show_ascii(arr,low,mid,high):
  print("\nArray:",arr)
  pointer_line = [" "] * len(arr)
  pointer_line[low] = "L"
  pointer_line[mid] = "M"
  pointer_line[high] = "H"

  print("      " + " ".join(pointer_line))
  print(f"low={low}, mid={mid}, high={high}")
  print("-" * 40)


def binary(arr,key):
  low = 0
  high = len(arr) - 1 #arr length 10 but index 0 -> 9 
  #// gives the floor value
  step = 1
  while low<=high:
    mid = (low + high) // 2
    print(f"\nStep:{step}")
    show_ascii(arr,mid,low,high)
    if arr[mid] == key:
      print(f"Found {key} at index {mid}")
      return mid
    elif arr[mid] < key:
      print(f"{key} > {arr[mid]} -> Move Right")
      low = mid + 1
    else:
      print(f"{key} < {arr[mid]} -> Move Left")
      high = mid - 1
    step +=1
  return -1

arr = [1,2,3,4,5,6,7,8,9,10]
key = 7

binary(arr,key)

