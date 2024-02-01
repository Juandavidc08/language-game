# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Library from google translator that will be used for the game
from googletrans import Translator
import random

print("----------------------------------------------------------")
print("             WELCOME TO THE LANGUAGE GAME               \n")
print("----------------------------------------------------------")
print("Today we will test your basic Spanish knowledge\n")
print("You will receive a set of 10 words.")
print("Your task is to translate them from Spanish into English.")
print("For every correct translation, you will earn a point.")
print("Try to complete all 10 questions in a consecutive manner.\n")
print("----------------------------------------------------------")
answer = input("Are you ready to play the Quiz? (y/n): \n")
score = 0
total_questions = 10

# Function to read words from a file


def search_words(file_name):
    with open(file_name, "r") as file:
        # Split the content into lines
        words = file.read().splitlines()
    return words


words = search_words("words.txt")
word = random.choice(words)

# Function to find word translation in Spanish


def translate_word(word):
    translation = translator.translate(word, src="es")
    return translation.text

# Questions function


def game_questions(quest_num, word):
    #input for question Loop
    user_answer = input(f"Q-{quest_num}:How do you say in English '{word}'?\n")

    translation = translate_word(word)

    if user_answer.lower() == translation.lower():
        global score
        score += 1
        print("That is correct! Great job!")
        print(f"Your score is: {score} correct answers\n")
    else:
        print(f"Wrong answer. The correct answer is {translation}")
        print(f"Your score is: {score} correct answers\n")

# Question loop


def game_loop():
    """
     Variable to identifly which words have already being
     seen in the game an remove them so it doesnt repeat
     """
    remaining_words = list(words)

    """
    range of values that quest_number will take
    It will starts from 1 and goes up to 10
    """
    for quest_num in range(1, total_questions + 1):
        if not remaining_words:
            print("Error: Not enough words in the list.")
            break

        word = random.choice(remaining_words)
        game_questions(quest_num, word)
        """
        take out the last word that it is used
        so it doesn't appear again
        """
        remaining_words.remove(word)
    end_game()

# End Game


def end_game():
    print("----------------------------------------------------------")
    print("                      ¡¡CONGRATULATIONS!!                ")
    print(f"             Your final score is: {score} out of 10")
    print("----------------------------------------------------------")
    print("If you want to restart the game press the letter (r)")
    print("If you want to exit press any other key")
    print("----------------------------------------------------------")
    # Input to restart the game
    end_answer = input("")
    if end_answer.lower() == "r":
        print("----------------------------------------------------------")
        print("                  GOOD LUCK - LETS DO IT!!           ")
        print("----------------------------------------------------------")
        game_loop()
    else:
        print("----------------------------------------------------------")
        print("             Thanks for playing, see you next time.")
        print("                       Exiting the game...        ")
        print("----------------------------------------------------------")

# Google API translator


translator = Translator()

# Start Game
if answer.lower() == "y":
    game_loop()
else:
    print("You did not choose 'yes.' Exiting the game.")
