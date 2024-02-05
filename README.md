THE LANGUAGE GAME
---

Welcome,

The language game is a pyhton terminal game, which runs in the Code Institute mock terminal on Heroku.

The purpose of this game is learning while playing, the user will chose the language they want to play with
and they will have to translate to english (EN) some random words they will be given.

The game consist in 10 questions and every correct answer the user will earn a point.

Try to complete all 10 questions! 

[Link to The Language Game](https://the-language-game-4bf6dd38ccc8.herokuapp.com/)
---
![Responsive Mockup](documentation/images/resposive-design.png)
---

## How to play

- The user enter to the game and they are give the set of instructions 
- Its given a choice to start game (y) 
- The player need to decide in which language you want to try their knowledge:
  - 1. Spanish
  - 2. French
  - 3. Italian
  - 4. German
- This answer needs to be numeric ex: Spanish is number 1.
- After, the player will need to answer 10 questions translating the word that is "shown" into english
- Finally th player will be able to check their scores and will be able to restart the challenge.

![Flow-Chart, Architecture- diagram of the game](documentation/images/arch-diagram-flow-chart.png)

- The point of this game is to enjoy, learn and check your basic knowledge in different languages, the words 
provided are easy and usefull words to know and understand.

## Feauters

### Existing Features

- Permanent use of Google Translator API, generating the translator this way
- Random word searcher
- Every question on one game the player will recieve a random question from a list depending on the language
- Also, if the answer is correct the player will have +1 score 
  but if its wrong it will be provided the correct answer to practice.

![Random question](documentation/random-quest.png)
![Wrong question](documentation/images/wrong-question.png)

- Possibility to try knowledge in diferent languages
![language choice](documentation/images/posibilities-lang.png)

- Restart game, input vaidation and error checking 
![restart](documentation/images/restart.png)
![error](documentation/images/error.png)

### Future features

- More Laguages to learn
- Dificult choice levels 


## Data Model

### Global Variables:

* answer: input to start or skip the quiz.
* score: A global variable to keep track of the player's score.
* total_questions: The total number of questions in the quiz.
* words: List of words loaded depending on the language.
* word: A randomly chosen word from the list of words.

### Functions:

* search_spanish_words(file_name): Reads words from a file in Spanish.
* search_french_words(file_name): Reads words from a file in French.
* choose_language(): Asks the user to choose a language.
* translate_word(word, src=""): Uses Google Translate to get the translation of a word.
* game_questions(quest_num, word, src=""): Asks the user a question and checks the answer.
* game_loop(): The main loop that iterates through the game questions.
* end_game(): Displays the final score and asks if the player wants to restart or exit.

### Google Translate API:

* translator: An instance of the Google Translate API for translating words.


## Testing

## Bugs

## Deployment

## Credits