#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
chosen_word = random.choice(word_list)
guess = input("pls guess a letter").lower()
lst =list(chosen_word)
display = []
for i in range(0,len(lst)):
  if lst[i] == guess:
    print(lst[i])
  else:
    print('_')

for i in range(0, len(lst)):
  display += "_"

for i in range(0, len(lst)):
  if lst[i] == guess:
    display[i] = guess
  





print(chosen_word)
print(display)
