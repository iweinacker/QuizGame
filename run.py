from Question import Question as qt

question_quiz = [
    "1. What kind of fish is Nemo?\n A) Shark\n B) Clownfish\n C) Whale\n \n",
    "2. Who is Ariels best friend in the Little Mermaid??\n A) Spongebob\n B) Poseidon\n C) Flounder\n \n",
    "3. Which school did Harry Potter attend? \n A) Hoggwart\n B) Harvart\n C) Homeschool\n \n",
    "4. What kind of animal is Simba? \n A) Dog\n B) Tiger\n C) Lion\n \n",
    "5. What is Shrek?\n A) An ogre\n B) A prince\n C) A donkey\n \n"
]
# defining the right answer in the question array
questions = [
    qt(question_quiz[0], "b"),
    qt(question_quiz[1], "c"),
    qt(question_quiz[2], "a"),
    qt(question_quiz[3], "c"),
    qt(question_quiz[4], "a"),
]

# Start game function

startGame = input("Do you want to play this awesome quizgame? (yes or no):")

if startGame != "yes":
    quit()

print("let's play\n")

# defining the function for the quiz game and showing the score


def play_game(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        correctAnswer = int((score/len(questions))*100)
    print("Your score is: "+str(correctAnswer)+"%")


play_game(questions)

# defining play again function


def play_again():
    response = input("Do you want to play again? (yes or no):")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False


while play_again():
    play_game(questions)

print("Have a nice day!!!")
