class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        response = input(
            f"Q.{self.question_number}: {current_question.text} (True/False)?: "
        ).capitalize()
        self.keep_score(response, current_question)

    def keep_score(self, user_answer, correct_answer):
        if user_answer == correct_answer.answer:
            self.score += 1
            print(
                f"You got it right!\nThe correct answer was {correct_answer.answer}\nYour current score is {self.score}/{self.question_number}"
            )
        else:
            print(
                f"You did not get that right.\nThe correct answer was {correct_answer.answer}\nYour current score is {self.score}/{self.question_number}"
            )
