#anagram => gum and mug . words are rearranges to make a new word
inp1 = input("Enter the first word:").lower().replace(" ","")
inp2 = input("Enter the second word:").lower().replace(" ","")
sorted_list1 = sorted(inp1)
sorted_list2 = sorted(inp2)

if sorted_list1 == sorted_list2:
  print("It is anagram")
else:
  print("Not anagram")