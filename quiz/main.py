from data import question_data
from question_model import Question
from quiz_brain import Brain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = Brain(question_bank)


while quiz.remaining_question():
    quiz.next_question()


print("your quiz are complete ")
print(f"your final Score is: {quiz.score}/{quiz.question_number}")