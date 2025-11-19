text = input("Enter the plain/encrypted text text:")
shift = int(input("Enter the shift:"))
choice = input("Enter the choice:\n1.Encryption\n2.Decryption\n")

number = [ord(c.upper())-ord('A') for c in text]

if choice == "1":
      cipher_number = ([(n + shift) % 26 for n in number])
      cipher_text = ''.join(chr(n + ord('A')) for n in cipher_number)
      print(cipher_text)
else:
      plain_number = ([(n -shift)%26 for n in number])
      plaintext = ''.join(chr(n + ord('A')) for n in plain_number)
      print(plaintext)

# number = 0
# letter = chr(number + ord('A'))

#ORD -> Ordina that returns the unicode for a single character
