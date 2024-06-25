import tkinter,tkinter.messagebox, random, json


class ProgramGUI:

    def __init__(self):
        self.main=tkinter.Tk()
        self.main.title("Quiz")
        self.main.geometry("450x450")
        self.main.resizable(False, False)
        self.correct=0
        self.incorrect=0
        self.count=0
        self.total=0
        self.max_total=0

        # Create the labels for question number, question text, and difficulty
        self.question_number=tkinter.Label(self.main, text="", font=("Calibri 20 bold")) #question number labl
        self.question_number.grid(row=0, column=0, columnspan=3)
        
        self.question_label = tkinter.Label(self.main, text="", font=("Verdana 23"),wraplength=400) 
        self.question_label.grid(row=1, column=0, columnspan=3)

        self.question_diffculty = tkinter.Label(self.main, text="", font=("Calibri 20")) 
        self.question_diffculty.grid(row=2, column=0, columnspan=3)

  

        self.givenAnswer=tkinter.StringVar()
        
        # Create the entry field and submit button for answers
        answerEntry=tkinter.Entry(self.main,textvariable=self.givenAnswer,font='arial 20') 
        submitButton = tkinter.Button(self.main,text="Submit",font='arial 20',command=self.check_answer)
        answerEntry.bind('<Return>', self.check_answer)
        answerEntry.grid(row=3, column=0, pady=2, padx=10) 
        submitButton.grid(row=3, column=1, pady=2, padx=10)
       
        # Load questions from the data file
        try:
            file=open(r'data.txt', 'r')
            self.data=json.load(file)
            random.shuffle(self.data)
            file.close()
        except(FileNotFoundError,json.JSONDecodeError):
            tkinter.messagebox.showerror("Missing/Invalid file")
            return
        if len(self.data)<5:
            tkinter.messagebox.showerror("“Insufficient number of questions")
            return
        
        # Display the first question
        self.show_question()
           
        tkinter.mainloop()


    def show_question(self):
        # Display the current question number and details
        question_number = f"Question {self.count + 1} of 5"
        self.diffculty=self.data[self.count]['difficulty']
        self.question_number.config(text=question_number, font=("Calibri", 14), fg="blue")
        self.question_label.config(text=self.data[self.count]['question'])
        
        # Display the difficulty level of the current question
        if self.diffculty==1:
            self.question_diffculty.config(text="This is an easy question!", font=("Calibri", 10), fg="blue")
        elif self.diffculty==2:
            self.question_diffculty.config(text="This is an medium question!", font=("Calibri", 10), fg="blue")
        else:
            self.question_diffculty.config(text="This is an hard question!", font=("Calibri", 10), fg="blue")

   
    # based on the question diffculty calculate the max possible score
    def max_score(self):        
        if self.diffculty==1:
            self.max_total+=1
        elif self.diffculty==2:
            self.max_total+=2
        elif self.diffculty==3:
            self.max_total+=3
        return self.max_total


    # Check the user's answer and update the score
    def check_answer(self,event=None):   
        user_answer = self.givenAnswer.get().strip()
        if not user_answer:
            tkinter.messagebox.showerror("Error", "Please enter your answer.")
            return
        possible_answers = self.data[self.count]['answers']

        max_total=self.max_score()
    
        if user_answer.strip().lower() in [answer.lower() for answer in possible_answers]:
            if self.data[self.count]['correct']==0:
                tkinter.messagebox.showinfo("Correct","Correct\nYou are the first person to answer this question!")
            else:
                tkinter.messagebox.showinfo("Correct","Correct")
            state=True
            self.correct+=1
            if self.diffculty==1:
                self.total+=1
            elif self.diffculty==2:
                self.total+=2
            else:
                self.total+=3
        else:
            tkinter.messagebox.showinfo("Incorrect","Incorrect")
            state=False
            self.incorrect+=1
            
        if state:
            self.data[self.count]['correct'] += 1
        else:
            self.data[self.count]['incorrect'] += 1
        
        self.count += 1
        self.givenAnswer.set("")
        
        if self.count!=5:
            self.show_question()
        else:
            file_write=open(r'data.txt', "w")
            json.dump(self.data, file_write, indent=4)
            tkinter.messagebox.showinfo("Game Over", f"You have completed all questions.\nCorrect: {self.correct}\nIncorrect: {self.incorrect}\nTotal Score: {self.total}\\{max_total}")
            self.main.destroy()

gui = ProgramGUI()



# If you have been paid to write this program, please delete this comment.
