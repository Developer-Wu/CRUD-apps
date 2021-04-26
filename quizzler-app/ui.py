from tkinter import *
from PIL import ImageTk, Image
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.window = Tk()
        self.quiz_brain = quiz_brain
        self.window.config(padx = 20, pady = 20, bg= THEME_COLOR, width= 250, height= 300)
        self.window.title('Quizzler')
        self.canvas = Canvas(width = 300, height = 250, highlightthickness=0)
        self.canvas.config()
        self.question = self.canvas.create_text(150,125,font= ('Arial',20,'italic'),text='Hello', width= 275)
        self.canvas.grid(column = 1, columnspan = 2, row= 2, padx=20, pady=20)
        self.tick_image = ImageTk.PhotoImage(Image.open('images/true.png'))
        self.tick_button = Button(image=self.tick_image, command=self.click_true)
        self.tick_button.config(highlightthickness= 0)
        self.tick_button.grid(column=1, row=3,pady= 20)
        self.cross_image = ImageTk.PhotoImage(Image.open('images/false.png'))
        self.score_label = Label(text= 'Score: 0',highlightthickness = 0, bg = THEME_COLOR, fg= 'white')
        self.score_label.grid(column=2,row=1,)

        self.cross_button = Button(image=self.cross_image,highlightthickness=0, command= self.click_false)
        self.cross_button.grid(column=2, row=3,pady= 20)
        self.change_question()
        self.window.mainloop()

    def change_question(self):
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question, text= q_text)
        else:
            self.canvas.itemconfig(self.question, text= 'You\'ve reached the end of the quiz')
            self.tick_button.config(state='disabled')
            self.cross_button.config(state='disabled')

    def click_true(self):
        answer = self.quiz_brain.user_answer = 'True'
        is_correct= self.quiz_brain.check_answer(answer)
        score = self.quiz_brain.score
        self.change_question()
        self.score_label.config(text=f'Score: {score}')
        self.give_feedback(is_correct)
        self.window.after(1000, func=self.return_normal)


    def click_false(self):
        answer = self.quiz_brain.user_answer = 'False'
        is_correct = self.quiz_brain.check_answer(answer)
        score = self.quiz_brain.score
        self.change_question()
        self.score_label.config(text=f'Score: {score}')
        self.give_feedback(is_correct)
        self.window.after(1000, func=self.return_normal)

    def return_normal(self):
        self.canvas.config(bg='white')


    def give_feedback(self, correct):
        if correct:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')






