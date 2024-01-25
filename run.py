# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Library from google translator that will be used for the game
from googletrans import Translator, constants
from pprint import pprint
# Being able to create random choices 
import random

print("Welcome to The Language Game\n")
print("Today we will test our basic spanish knowledge\n")
print("You will receive a set of 10 questions, each featuring a different word. Your task is to translate these words into Spanish. For every correct translation, you will earn a point towards your score. Try to complete all 10 questions in a consecutive manner.")
answer = input("Are you ready to play the Quiz ? (yes/no) :")
score = 0 
total_questions = 10

#functions to read words from a file 
def search_words(file_name):
    with open(file_name, "r") as a file:
        #slipt the content into lines
        words = file.read().splitlines()
    return words

words = search_words("words.txt")
word = random.choice(words)

