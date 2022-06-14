rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
player_choise  = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
com_choise = random.randint(0,2)
if player_choise == "0" and com_choise == 0:
  print(f"Your choise: {rock}")
  print(f"computer choise: {rock}")
  print("It's a draw")
elif player_choise == "0" and com_choise == 1:
  print(f"Your choise: {rock}")
  print(f"computer choise: {paper}")
  print("You Lose")
elif player_choise == "0" and com_choise == 2:
  print(f"Your choise: {rock}")
  print(f"computer choise: {scissors}")
  print("You Win")
elif player_choise == "1" and com_choise == 0:
  print(f"Your choise: {paper}")
  print(f"computer choise: {rock}")
  print("It's a draw")
elif player_choise == "1" and com_choise == 1:
  print(f"Your choise: {paper}")
  print(f"computer choise: {paper}")
  print("You Win")
elif player_choise == "1" and com_choise == 2:
  print(f"Your choise: {paper}")
  print(f"computer choise: {scissors}")
  print("You Lose")
elif player_choise == "2" and com_choise == 0:
  print(f"Your choise: {scissors}")
  print(f"computer choise: {rock}")
  print("You Lose")
elif player_choise == "2" and com_choise == 1:
  print(f"Your choise: {scissors}")
  print(f"computer choise: {paper}")
  print("You Win")
elif player_choise == "2" and com_choise == 2:
  print(f"Your choise: {scissors}")
  print(f"computer choise: {scissors}")
  print("It's a draw")
else:
  print("Invalid number\n You Lose")
