# QuizGame

QuizGame is a Python terminal game, which runs in the Code institue mock terminal on Heroku

Users can participate in a trivia game in which they have to answer different questions of all kinds. It has a total of 5 questions but has the possibility to be as many as you want.

The live link can be found [here](https://quiz-game-project-f9cd2923ecb8.herokuapp.com/)

![image](https://github.com/iweinacker/QuizGame/assets/130374663/ff419db2-b509-41bd-a446-0e9b3c13d1a5)

## How to play it?

The rules for QuizGame are simple. At the beginning it asks you if you want to play, if you answer "yes", the trivia game will start, but if you answer "no", the game will stop. 

Different questions of all kinds will appear, and you will have the option to choose the answer "a", "b" or "c". As you answer the questions, other questions will start to appear with a total of 5 questions. 

## features

At the beginning and as a cover, the game asks you if you want to start the trivia, having the option "yes" or "no". 

![image](https://github.com/iweinacker/QuizGame/assets/130374663/2fd6ddc1-736b-4f0f-9eec-f616a681eb97)

In the case of "no" the game is over, and in the case of "yes" the phrase "let's go!" appears together with the first question.

![image](https://github.com/iweinacker/QuizGame/assets/130374663/7261aecc-d055-4881-88a7-44e27bb6d485)

As you answer the questions, regardless of whether they are correct or not, the following questions will be displayed. 

![image](https://github.com/iweinacker/QuizGame/assets/130374663/5bc06d48-e1a6-46ad-bc58-f356a1f61d33)

At the end of the questions, the percentage of correct answers will appear. 

![image](https://github.com/iweinacker/QuizGame/assets/130374663/c22fa99a-a1d4-44bb-957f-77c91d013bd4)

At the end of the trivia game you will be asked "Do you want to play again? (yes or no)" in which, if you are not satisfied with your result, you can enter "yes" which will start the trivia game again, if not, you will be asked "Have a nice day!!!" and the game will end.

![image](https://github.com/iweinacker/QuizGame/assets/130374663/d29812da-449b-4385-91c3-322b959c09c5)


## Testing

I have manually tested this project doing the following:

- Passed the code through a PEP8 linter and confirmed the problems it might have.
- Tested in my locas terminal and the Code Institute Heroku terminal.
- Given the different inputs possible to se how it respond.

### Remaining Bugs

It has two bugs regarding the line length, but these are related to the questions and alternatives so it does not affect the project itself.

- 5: E501 line too long (107 > 79 characters)
- 6: E501 line too long (96 > 79 characters)


## Deployment

This project was deployed using Code Institute's mock terminal for Heroku

- Steps for deployment:
  - Fork or clone this repository
  - Create a Heroku app
  - Set the buildbacks to Python and NodeJS in that order
  - Link the Heroku app to the repository
  - Click on #Deploy 

## Credits

### content
- Code Institute for the material and the deploy terminal
- [Bro Code for the play again idea](https://www.youtube.com/watch?v=yriw5Zh406s)
- Teaching expertise for the [trivia questions and answers] examples(https://www.teachingexpertise.com/classroom-ideas/easy-quiz-questions-and-answers/)
  

