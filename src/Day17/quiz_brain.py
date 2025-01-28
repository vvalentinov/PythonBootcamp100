class QuizBrain:

    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        curr_question = self.question_list[self.question_number]

        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {curr_question.text} (True/False)?: ")
        while not user_answer in ("True", "False"):
            print("You have to choose either 'True' or 'False'. Type again.")
            user_answer = input(f"Q.{self.question_number}: {curr_question.text} (True/False)?: ")

        self.check_answer(user_answer, curr_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right! Congratulations!")
            self.score += 1
        else:
            print("That is wrong. No biggie, you'll get them next time.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")