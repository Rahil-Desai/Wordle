import random
import os

clear = lambda: os.system('clear')
from termcolor import colored
import words

secret_word = random.choice(words.words)
global tries

guess = 0
correct = False
print("Wordle\n\nEnter Guesses:\n")
while guess < 6 and not correct:
  guessword = input('')
  while len(guessword) != 5:
    print("Please enter a 5 letter word")
    guessword = input('')
    print('\033[1A' + '\033[K', end='')
    print('\033[1A' + '\033[K', end='')
  print('\033[1A' + '\033[K', end='')
  guess += 1
  position = 0
  clue = ""
  used = ""
  for letter in guessword:
    if letter == secret_word[position]:
      clue += colored(letter, 'light_green')
    elif letter in secret_word:
      clue += colored(letter, 'light_yellow')
    else:
      clue += colored(letter, 'grey')
      used += letter
    position += 1
  print(clue)
  if guessword == secret_word:
    correct = True
    print("Congratulations! You guessed the correct word in", guess,
          "guesses!")
    break
else:
  print("The word was", secret_word)