from Question import Question as qt

question_quiz = [
    "1. What kind of fish is Nemo?\n A) Shark\n B) Clownfish\n C) Whale\n \n",
    "2. Who is Ariels best friend in the Little Mermaid??\n A) Spongebob\n B) Poseidon\n C)  Flounder\n \n",
    "3. Which school did Harry Potter attend? \n A) Hoggwart\n B) Harvart\n C) Homeschool\n \n",
    "4. What kind of animal is Simba? \n A) Dog\n B) Tiger\n C) Lion\n \n",
    "5. What is Shrek?\n A) An ogre\n B) A prince\n C) A donkey\n \n"
]

questions = [
    qt(question_quiz[0], "b"),
    qt(question_quiz[1], "c"),
    qt(question_quiz[2], "a"),
    qt(question_quiz[3], "c"),
    qt(question_quiz[4], "a"),
]


def new_game(questions):
    guess = []
    score = []
    question_num = 1

    for question in questions:
        answer = input(question_quiz)
        if answer == question.answer:
            score += 1
        print("Congratulations!!, you got" + str(score) +
              "/" + str(len(questions)) + " correct")


new_game(questions)
