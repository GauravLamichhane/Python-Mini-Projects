"""
Number Guessing Game
→ Randomly generate a number; user keeps guessing until correct.
→ Add hints (“Too high / Too low”) and attempt count.
"""
import random
attempt_count = 5
number = random.randint(1,100)
print("Welcome to the number guessing game")
while attempt_count > 0:
  user_number = int(input("Enter the number:"))
  if user_number == number:
    print("Congrats the number you have guessed is correct")
  elif user_number > number:
    print("Too High")
  else:
    print("Too Low")
  attempt_count -= 1
  print(f"Attempts left:{attempt_count}")
  print("Try again")
# print(number)
