#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word_choice = list(random.choice(word_list))
print(word_choice)

#Testing code
print(f'Pssst, the solution is {word_choice}.')

#TODO-4: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for char in word_choice:
    display.append("_")

print(display)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
print(guess)

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# 3rd attempt - 4 lines better than 1st attempt
# 2nd attempt used a count variable
#TODO-5: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
count = 0
for char in word_choice:
    if char == guess:
        print("Right")
        display[count] = guess
    else:
        print("Wrong")
    count += 1

# 1st attempt no hint - works but could be more 
# efficiently written
# word_choice_len = len(word_choice)
# print(word_choice_len)
# count = 0
# while count < word_choice_len:
#     if guess == word_choice[count]:
#         print("Right")
#     else:
#         print("Wrong")
#     count += 1

#TODO-6: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

print(display)