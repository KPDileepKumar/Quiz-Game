from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("Quizzler")
        self.window.configure(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=50, pady=50)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        image_1 = PhotoImage(file="images/true.png")
        image_2 = PhotoImage(file="images/false.png")
        self.right = Button(image=image_1, command=self.check_for_true, highlightthickness=0)
        self.right.grid(row=2, column=0)
        self.wrong = Button(image=image_2, command=self.check_for_false, highlightthickness=0)
        self.wrong.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        self.score_label.configure(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Quiz has got completed\nScore: {self.quiz.score}")
            self.right.configure(state="disabled")
            self.wrong.configure(state="disabled")

    def check_for_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_for_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, solution):
        self.window.after(1000, self.get_next_question)
        if solution:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
