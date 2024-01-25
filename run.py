# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Library from google translator that will be used for the game
from googletrans import Translator
import random

print("Welcome to The Language Game\n")
print("Today we will test your basic Spanish knowledge\n")
print("You will receive a set of 10 words, each featuring a different word. Your task is to translate these words from Spanish into English. For every correct translation, you will earn a point towards your score. Try to complete all 10 questions in a consecutive manner.")
answer = input("Are you ready to play the Quiz? (y/n): ")
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
def game_questions(word):
    user_answer = input(f"First Question 1: How do you say in Spanish '{word}'?\n")

    translation = translate_word(word)

    if user_answer.lower() == translation.lower():
        global score
        score += 1
        print("That is correct! Great job!")
        print(f"Your score is: {score} correct answers")
    else:
        print(f"Wrong answer. The correct answer is {translation}")
        print(f"Your score is: {score} correct answers")

# Google API translator
translator = Translator()

#Start Game
if answer.lower() == "y" :
    game_questions(word)
else:
    print("You did not choose 'yes.' Exiting the game.")
