import random
import hangman_art
import hangman_words
from replit import clear
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

guess_list = []
for letter in chosen_word:
  guess_list += '_'

end_of_game = False
lives = 6
print(hangman_art.logo)
while (end_of_game != True):
  
  guess = input("Guess a letter: ").lower()
  clear()
  for letter in range(0,len(chosen_word)):
    if guess == chosen_word[letter]:
      guess_list[letter] = guess
  
  if not guess in chosen_word:
    lives -= 1
    print(hangman_art.stages[lives])
  
  print(guess_list)
  
  if not "_" in guess_list:
    end_of_game = True
    print("You Win")
    print(hangman_art.win)
  elif lives <= 0:
    end_of_game = True 
    print("You Lose")



