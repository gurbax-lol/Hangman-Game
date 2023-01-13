# Hangman 
# Some source code and art by Angela Yu from London App Brewery, as part of their Python Pro Bootcamp https://www.londonappbrewery.com/

from replit import clear
import random
import hangman_words
import hangman_art

print(hangman_art.logo)
category = input("Pick a category: birds / movies / countries\n").lower()
word_list = []
if category == "birds":
  word_list = hangman_words.birds
elif category == "movies":
  word_list = hangman_words.movies
elif category == "countries":
  word_list = hangman_words.countries

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in chosen_word:
      print("You've already guessed that letter.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"{guess} is not in the chosen word.")
        lives -= 1
        if lives > 1:
          print(f"Lives left: {lives}")
        else:
          print("LAST LIFE!")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was: {chosen_word}")

    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
