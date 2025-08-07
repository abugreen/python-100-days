class QuizBrain:
    def __init__(self, q_list):
        self.q_list = q_list
        self.question_number = 0
        self.question_answer = ""
        self.correct_number = 0
        
    def next_question(self):
        self.question_answer = input(f"Q.{self.question_number+1}: {self.q_list[self.question_number].text} (True/False)? : ")
        if self.question_answer == self.q_list[self.question_number].answer:
            self.correct_number += 1
            print("You got it right")
            print(f"The correct answer was: {self.q_list[self.question_number].answer}")
            print(f"Your current score is: {self.correct_number}/{self.question_number+1}")
        else:
            print("You got it wrong")
            print(f"The correct answer was: {self.q_list[self.question_number].answer}")
            print(f"Your current score is: {self.correct_number}/{self.question_number+1}") 
        self.question_number += 1
        
    def still_has_questions(self):
       question_total_number = len(self.q_list)
       print(question_total_number)
       print(self.question_number)
       if question_total_number == self.question_number:
            return False
       else:
            return True
