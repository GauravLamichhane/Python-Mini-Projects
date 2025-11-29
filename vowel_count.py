"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
import operator as op
def get_count(sentence):
  count = 0
  vowels = 'aeiouAEIOU'
  for ch in sentence:
    if ch in vowels:
      count += 1

  return count

            


user_sentence = input("Enter the sentence:")
print(get_count(sentence = user_sentence))