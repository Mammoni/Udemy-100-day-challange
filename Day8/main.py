from replit import clear
import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encript(text,shift):
  cipher_text = ""
  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = ((position+shift)%26)
      new_letter = alphabet[new_position]
      cipher_text += new_letter
    else:
      position = letter
      cipher_text += position
  print(cipher_text)

def decript(text,shift):
  cipher_text = ""
  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = ((position-shift)%26)
      new_letter = alphabet[new_position]
      cipher_text += new_letter
    else:
      position = letter
      cipher_text += position
  print(cipher_text)
  
def cezar(text,shift,direction):
  if direction == "encode":
    encript(text,shift)
  elif direction == "decode":
    decript(text,shift)
  else:
    print(f"Wrong input {direction}")
    
program_run = "yes"
while program_run != "no":
  print(art.logo)
  if program_run == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cezar(text,shift,direction)
    program_run = input("Want to continue Yes/No?:\n").lower()
    clear()
  else:
    print("Wrong input!")
    

 
