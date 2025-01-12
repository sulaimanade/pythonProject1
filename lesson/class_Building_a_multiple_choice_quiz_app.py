from class_Building_a_multiple_choice_quiz import Question
question_prompts = [
    "What color are Apples?\n(a) Red/Green\n(b) Purple\n(c) Black\n\n",
    "What color are Banana?\n(a) Blue\n(b) Pink\n(c) Yellow \n\n",
    "What color are Strawberries?\n(a) Black\n(b) Red\n(c) Yellow\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)