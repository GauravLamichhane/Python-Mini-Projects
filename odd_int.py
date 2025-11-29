def find_it(seq):
  for item in seq:
    if seq.count(item) %2 !=0:
      return item
print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))