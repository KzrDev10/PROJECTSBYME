from data import question_data
from Question_model import Question
from Quiz_Brain import Quiz_Brain
import random

question_bank = []


for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)


print("Welcome to my Quiz game type True or False:")
print("There are 200 questions in this quiz, Type end to stop game")


quiz = Quiz_Brain(question_bank)

while quiz.still_has_questions: 
    quiz.next_question()