import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(pady=50, padx=50, bg=THEME_COLOR)

        # Score Label
        self.score_label = tk.Label(
            text=f"Score: {self.quiz_brain.score}",
            bg=THEME_COLOR,
            fg="white",
            font=("Ariel", 15))
        self.score_label.grid(row=0, column=1, pady=(0, 30))

        # Canvas
        self.canvas = tk.Canvas()
        self.canvas.config(height=400, width=500)
        self.question_text = self.canvas.create_text(
            250,
            200,
            text="",
            font=("Arial", 20, "italic"),
            width=480,
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=(0, 30))

        # Images
        check_img = tk.PhotoImage(file="images/true.png")
        false_img = tk.PhotoImage(file="images/false.png")

        # Buttons
        self.true_button = tk.Button(image=check_img,highlightthickness=0)
        self.true_button.config(cursor="hand2", command=self.on_true_btn_click)
        self.true_button.grid(column=0, row=2)

        self.false_button = tk.Button(image=false_img, highlightthickness=0)
        self.false_button.config(cursor="hand2", command=self.on_false_btn_click)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            next_question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=next_question)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def on_true_btn_click(self):
        is_correct = self.quiz_brain.check_answer(user_answer="true")
        self.give_feedback(is_correct)

    def on_false_btn_click(self):
        is_correct = self.quiz_brain.check_answer(user_answer="false")
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct: bool):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)