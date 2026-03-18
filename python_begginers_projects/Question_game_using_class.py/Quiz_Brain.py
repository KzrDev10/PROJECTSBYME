class Quiz_Brain:
    def __init__(self,questions):
        self.questions = questions
        self.q_num = 0
        self.score = 0
    
    def next_question(self):
        current_question = self.questions[self.q_num]
        self.q_num += 1
        user_ans = input(f"Q{self.q_num}: {current_question.text} (True/False): ")
        self.check_answer(user_ans,current_question.answer)

    def still_has_questions(self):
        if self.q_num < len(self.questions):
            return True
        else:
            return False
        # or just return self.q_num < len(self.questions)

    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct")
            self.score += 1
            print(f"Your score is {self.score}/{self.q_num}\n")
        else:
            print("Wrong")
            print(f"Correct answer was {correct_answer}\n")
        if user_answer.lower() == "end":
            self.still_has_questions == False