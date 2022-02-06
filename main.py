#Step 1 
import random
from hangman_words import word_list
from hangman_art import logo, stages

end_of_game = False
word_choice = list(random.choice(word_list))
word_length = len(word_choice)
lives = 6

print(logo)

#Testing code
#print(f'Pssst, the solution is {word_choice}.')

# Create the blanks
display = []
for char in word_choice:
    display.append("_")

print(display)

while not end_of_game:
    # get a guess from the user
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already chosen the letter: {guess}.\nPlease choose another letter.")

    # check the guess against the word choice
    if guess in word_choice:
        for position in range(word_length):
            letter = word_choice[position]
            if letter == guess:
                display[position] = guess

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    if guess not in word_choice:
        print(f"The letter '{guess}'' is not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game == True
            print("You lose.")

    print(stages[lives])