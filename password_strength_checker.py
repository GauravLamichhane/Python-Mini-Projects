"""
a pass is strong if it has
uppecase
lowercase
number
special symbols
if 0f min 8 
has digit
"""
passw = input("Enter the pasword:")
print(passw)
has_lower = False
has_upper = False
has_digit = False
has_special = False
special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"
for char in passw:
  if char.islower():
    has_lower = True
  elif char.isupper(): has_upper = True
  elif char.isdigit(): has_digit = True
  elif char in special_chars : has_special = True

if len(passw) < 8:
  print("Password too short!")
elif not has_upper:
  print("Add at least one upper case letter")
elif not has_lower:
  print("Add atleast one lower case letter")
elif not has_digit:
  print("Add at least one digit")
elif not has_special:
  print("Add at least one special character")
else:
  print("Strong Password")