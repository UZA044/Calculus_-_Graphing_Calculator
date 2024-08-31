#Tkinter is imported for GUI
#datetime module imported
#matplotlib imported for use in graphing calculations
#numpy and sympy imported to carry out differentiation and integration
#for complex calculations page
import tkinter as tk
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from client import *


# different Font sizes
small_font = ("Calibri", 15)
small2_font = ("Calibri", 13)
smaller_font = ("Calibri", 10)
large_font = ("Calibri", 40, "bold")
largesymp_font = ("Calibri", 50, "bold")
dig = ("Calibri", 23, "bold")
norm = ("Calibri", 20)
big_complexfont = ("Calibri", 21, "bold")
display_font = ("Calibri", 30, "bold")
calc_font=("Calibri",30,"bold")

#simple calculator class creates tkinter window
class simplecalculator:
    def __init__(self, username):
        self.working_label = None
        self.answer_label = None
        self.window = tk.Tk()
        self.window.geometry("500x480")
        self.window.title("Calculator")
        self.window.wm_iconbitmap("calc.ico")
        self.window.configure(bg="Black")
        self.window.resizable(False, False)
        self.username = username
        self.call=client()


        # settting answer and working out to 0 at the start
        self.total_ex = ""
        self.current_ex = ""



        #runs the gui related code
        self.create_displaylabels()
        self.create_digit()
        self.operator_buttons()
        self.eq = 11

     # creating total and working out output labels which will display answers
    def create_displaylabels(self):
        self.working_label = Label(self.window, width=75, height=1,bg="black", text=self.current_ex, fg="White",anchor=tk.W,font=small_font)
        self.working_label.pack()
        self.answer_label = Label(self.window, width=75, height=3, bg="black",text=self.total_ex, anchor=tk.E,fg="Orange",font=calc_font)
        self.answer_label.pack()


    # creating AC command which clears the labels and updates them using self.uplabel and self.uptotal_label
    def ac(self):
        self.total_ex = ""
        self.current_ex = ""
        self.uplabel()
        self.uptotal_label()

    #creates digits on the gui for 0 to 9
    def create_digit(self):
        button = Button(self.window, text=str("0"), bg="Black", fg="Orange", font=dig, borderwidth=0, command=lambda k=0: self.add_ex(k),width=7)
        button.place(x=130, y=410)

        button = Button(self.window, text="1", bg="Black", fg="Orange", font=dig, borderwidth=0, command=lambda k=1: self.add_ex(k), width=7)
        button.place(x=5, y=340)
        button = Button(self.window, text="2", bg="Black", fg="Orange", font=dig, borderwidth=0, command=lambda k=2: self.add_ex(k), width=7)
        button.place(x=130, y=340)
        button = Button(self.window, text="3", bg="Black", fg="Orange", font=dig, borderwidth=0, command=lambda k=3: self.add_ex(k), width=7)
        button.place(x=250, y=340)

        button = Button(self.window, text="4", bg="Black", fg="Orange", font=dig, borderwidth=0, command=lambda k=4: self.add_ex(k), width=7)
        button.place(x=5, y=270)
        button = Button(self.window, text="5", bg="Black", fg="Orange", font=dig, borderwidth=0, command=lambda k=5: self.add_ex(k), width=7)
        button.place(x=130, y=270)
        button = Button(self.window, text="6", bg="Black", fg="Orange", font=dig, borderwidth=0, command=lambda k=6: self.add_ex(k), width=7)
        button.place(x=250, y=270)

        button = Button(self.window, text="7", bg="Black", fg="Orange", font=dig, borderwidth=0, command=lambda k=7: self.add_ex(k), width=7)
        button.place(x=5, y=200)
        button = Button(self.window, text="8", bg="Black", fg="Orange", font=dig, borderwidth=0, command=lambda k=8: self.add_ex(k), width=7)
        button.place(x=130, y=200)
        button = Button(self.window, text="9", bg="Black", fg="Orange", font=dig, borderwidth=0, command=lambda k=9: self.add_ex(k), width=7)
        button.place(x=250, y=200)
        button = tk.Button(self.window, text=str("."), bg="Black", fg="Orange", font=dig, borderwidth=0, command=lambda k='.': self.add_ex(k),width=7)
        button.place(x=5, y=410)







    #creates operator buttons on the gui for  + - - / AC and button for History
    def operator_buttons(self):
        button = tk.Button(self.window, text=str("AC"), bg="Black", fg="Orange", font=dig, borderwidth=0, command=self.ac,width=11)
        button.place(x=5, y=130)
        button = tk.Button(self.window, text=str("History"), bg="Black", fg="Orange", font=dig, borderwidth=0, command=self.histrun,width=10)
        button.place(x=190, y=130)
        button = tk.Button(self.window, text="\u00F7", bg="Black", fg="Orange", font=dig, borderwidth=0, command=lambda k="/": self.add_operator(k), width=8)
        button.place(x=370, y=130)
        button = tk.Button(self.window, text="\u00D7", bg="Black", fg="Orange", font=dig, borderwidth=0, command=lambda k="*": self.add_operator(k), width=8)
        button.place(x=370, y=200)
        button = tk.Button(self.window, text="-", bg="Black", fg="Orange", font=dig, borderwidth=0, command=lambda k="-": self.add_operator(k), width=8)
        button.place(x=370, y=270)
        button = tk.Button(self.window, text="+", bg="Black", fg="Orange", font=dig, borderwidth=0, command=lambda k="+": self.add_operator(k), width=8)
        button.place(x=370, y=340)
        button = tk.Button(self.window, text="=", bg="Black", fg="Orange", font=dig, borderwidth=0, command=self.final, width=16)
        button.place(x=250, y=410)




    # when called a value is taken as a parameter which is then added to the total expression and is then updated
    def add_ex(self, value):
        self.current_ex += str(value)
        self.uplabel()

    # this function takes in a operator as a paramter and then adds it to the current label
    # Where then it is also added to the working out label and updated both labels
    #used to add operators to display labels and send operator to be calculated
    def add_operator(self, operator):
        self.current_ex += operator
        self.total_ex += self.current_ex
        self.current_ex = ""
        self.uptotal_label()
        self.uplabel()

    #needed to update the labels with the correct expression
    def uptotal_label(self):
        self.working_label.config(text=self.total_ex)

    # called to update answer label
    def uplabel(self):
        self.answer_label.config(text=self.current_ex)

    # this is called by pressing the equals button
    # what this does is computes the expressions stored in working out label and then updates the answer display label
    # then the values stored in answer (total_Ex) is reset to prevent it being involved in next calculation
    def final(self):
        self.eq = +1

        self.total_ex += self.current_ex
        self.uptotal_label()
        self.current_ex = str(eval(self.total_ex))
        self.sql_add(self.total_ex, self.current_ex)
        self.total_ex = ""
        self.uplabel()

    # connects to sql to add the calculation and answers to the sql table
    #shown by connecting and calling class Client's send list method
    #list is sent with command to insert simple calculation
    #data is inserted to table
    def sql_add(self, calculation, answer):
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        list=["SIMPLE INSERT",self.username,calculation,answer,date]
        recieved=self.call.send(list)



    # called by pressing the history button and therefore runs the history window
    def histrun(self):
        self.test = History(self.username)
        self.test.select_simple()
        self.test.gui_simple()

    # runs the simple calculator window when called.
    def run(self):
        self.window.mainloop()

# class for complex calculations window
class complexcalculations:
    def __init__(self, username):

        # below the tkinter window for complex caluclations is being setup.
        self.answer = None
        self.row2 = None
        self.row = None
        self.row1 = None
        self.call=client()
        self.username = username
        self.window = tk.Tk()
        self.fix_buttons()
        self.window.geometry("800x700")
        self.window.title("Complex calculations")
        self.window.wm_iconbitmap("calc.ico")
        self.func = ""
        self.window.configure(background="black")
        self.create_top_frame()
        self.create_matrix_frame()
        self.create_bot_frame()
        self.create_entry()
        self.create_buttons()

    # the tkinter window for complex calculations is being fixed
    # by sorting the column and row config
    def fix_buttons(self):
        self.window.rowconfigure(1, weight=2)
        self.window.rowconfigure(2, weight=1)
        for i in range(0, 10):
            self.window.columnconfigure(i, weight=1)

    # this creates a frame for the output label at the bottom
    def create_bot_frame(self):
        self.frame2 = Frame(self.window, width=750)
        self.frame2.grid(row=2, column=0, padx=0, pady=0)

    #this creates matrix frame for matrix calculator
    #stores input boxes for matrix
    def create_matrix_frame(self):
        self.frame3 = Frame(self.window, width=700)
        self.frame3.grid(row=1, column=0, ipadx=400, ipady=50)
        self.frame3.configure(background="black")
        for i in range(0, 10):
            self.frame3.columnconfigure(i, weight=1)
        for i in range(0, 10):
            self.frame3.rowconfigure(i, weight=1)

    # this creates the top frame and fixes the column and row config
    #stores the rest of the functions such as differentiation etc
    def create_top_frame(self):
        self.frame1 = Frame(self.window, width=700)
        self.frame1.grid(row=0, column=0, ipadx=300, ipady=50)
        self.frame1.configure(background="black")
        for i in range(0, 10):
            self.frame1.columnconfigure(i, weight=1)
        for i in range(0, 10):
            self.frame1.rowconfigure(i, weight=1)

    # This function creates multiple labels and entries some for differentiation and integration as well as
    # matrixes inputs and factorial calculations.
    def create_entry(self):
        self.userlabel = Label(self.frame1, text=self.username, bg="black", fg="orange")
        self.userlabel.grid(column=8, row=0)

        self.factl = Label(self.frame1, text="Find the Factorial", bg="black", fg="orange", font=small_font)
        self.factl.grid(column=2, row=4)

        self.diffl = Label(self.frame1, text="Differentiation", bg="black", fg="orange", font=small_font)
        self.diffl.grid(column=2, row=0, padx=20)

        self.intl = Label(self.frame1, text="Integration", bg="black", fg="orange", font=small_font)
        self.intl.grid(column=6, row=0, padx=20)

        self.fact = tk.Entry(self.frame1, bd=5, bg="white", fg="black", width=16, font=small_font)
        self.fact.grid(column=2, row=5, padx=20)

        self.diffe = tk.Entry(self.frame1, bd=5, bg="white", fg="black", width=16, font=small_font)
        self.diffe.grid(column=2, row=1, padx=20)

        self.inte = tk.Entry(self.frame1, bd=5, bg="white", fg="black", width=16, font=small_font)
        self.inte.grid(column=6, row=1, padx=20)

        self.ans = Label(self.frame2, text="", bg="black", fg="orange", font=small_font)
        self.ans.grid(column=0, row=0)

        self.intlim = Label(self.frame1, text="Integration limits", bg="black", fg="orange", font=small_font)
        self.intlim.grid(column=6, row=4, padx=20)

        self.intelim1 = tk.Entry(self.frame1, bd=5, bg="white", fg="black", width=4, font=small_font)
        self.intelim1.grid(column=6, row=5, padx=0)

        self.intelim2 = tk.Entry(self.frame1, bd=5, bg="white", fg="black", width=4, font=small_font)
        self.intelim2.grid(column=7, row=5, sticky=tk.W, padx=20)

        self.matrix = Label(self.frame3, text="Matrix Calculator", bg="black", fg="orange", font=small_font)
        self.matrix.grid(column=5, row=2)

        self.matrix1a = tk.Entry(self.frame3, bd=5, bg="white", fg="black", width=16, font=small_font)
        self.matrix1a.grid(column=4, row=3)

        self.matrix1b = tk.Entry(self.frame3, bd=5, bg="white", fg="black", width=16, font=small_font)
        self.matrix1b.grid(column=4, row=4)

        self.matrix1c = tk.Entry(self.frame3, bd=5, bg="white", fg="black", width=16, font=small_font)
        self.matrix1c.grid(column=4, row=5)

        self.matrix2a = tk.Entry(self.frame3, bd=5, bg="white", fg="black", width=16, font=small_font)
        self.matrix2a.grid(column=6, row=3)

        self.matrix2b = tk.Entry(self.frame3, bd=5, bg="white", fg="black", width=16, font=small_font)
        self.matrix2b.grid(column=6, row=4)

        self.matrix2c = tk.Entry(self.frame3, bd=5, bg="white", fg="black", width=16, font=small_font)
        self.matrix2c.grid(column=6, row=5)

        self.matrix3 = tk.Entry(self.frame3, bd=5, bg="white", fg="black", width=16, font=small_font)
        self.matrix3.grid(column=5, row=4)



    # creates buttons so that data can be processed on the click for all functions
    def create_buttons(self):
        self.enter1 = tk.Button(self.frame1, text="Enter", command=self.diff, bg="black", fg="orange", height=1,width=8)
        self.enter1.grid(column=3, row=1, sticky=tk.W, padx=0)

        self.hist1 = tk.Button(self.frame1, text="History", command=self.check_hist1, bg="black", fg="orange", height=2,width=8)
        self.hist1.grid(column=0, row=0, sticky=tk.W, padx=0)

        self.enter3 = tk.Button(self.frame1, text="Enter", command=self.take_fact, bg="black", fg="orange", height=1,width=8)
        self.enter3.grid(column=3, row=5, sticky=tk.W, padx=0)

        self.enter2 = tk.Button(self.frame1, text="Enter", command=self.integ, bg="black", fg="orange", height=1,width=8)
        self.enter2.grid(column=7, row=1, sticky=tk.W, padx=0)

        self.enterlim = tk.Button(self.frame1, text="Enter", command=self.integlimits, bg="black", fg="orange",height=1, width=8)
        self.enterlim.grid(column=8, row=5, sticky=tk.W, padx=0)

        self.matrixbut = tk.Button(self.frame3, text="Enter", command=self.matrix_multiplication, bg="black",fg="orange", height=3, width=8)
        self.matrixbut.grid(column=8, row=5, sticky=tk.W, padx=0)

    #runs the history window for complex calculator
    def check_hist1(self):
        self.test = History(self.username)
        self.test.select_complex()
        self.test.gui_complex()

    # parameter in function is the answer which should be displayed on window
    def answer_label(self, answer):

        self.answer = str(answer)
        self.ans.config(text=self.answer)

    # Function called by factorial button
    #Use of exception handling to carry out factorial of number
    #if cannot be run prompt outputted
    #otherwise stores answer and input into calculations table
    def take_fact(self):
        n = self.fact.get()
        try:
            n=int(n)
            j = self.factorials(n)
            type = "factorial"
            self.add_hist(j, type, n)

            if len(str(j)) <= 30:
                self.answer_label(j)
            else:
                messagebox.showinfo("This is your answer displayed here", j)
        except:
            messagebox.showinfo("","Please enter a integer value")





    # factorial recursion function which returns factorial of a number
    def factorials(self, n):
        if n == 1 or n==0:
            return n
        else:

            result = n * self.factorials(n - 1)
            return result

    # carrys out matrix operations where it takes the data as arrays and make into multi dimesional array as
    # well as taking a operator to carry out operation on matrices
    def matrix_multiplication(self):
        try:
            #decider is the operator
            decider = self.matrix3.get()

            #These values are for matrix inputs
            xline1 = self.matrix1a.get()
            xline2 = self.matrix1b.get()
            xline3 = self.matrix1c.get()


            yline1 = self.matrix2a.get()
            yline2 = self.matrix2b.get()
            yline3 = self.matrix2c.get()

            lst1 = [int(item) for item in xline1.split()]
            lst2 = [int(item) for item in xline2.split()]
            lst3 = [int(item) for item in xline3.split()]

            #2 seperate matrixes are created by doiing a list operation above
            X = [lst1,
                lst2,
                lst3]

            lst4 = [int(item) for item in yline1.split()]
            lst5 = [int(item) for item in yline2.split()]
            lst6 = [int(item) for item in yline3.split()]

            #2nd matrix
            Y = [lst4,
                lst5,
                lst6]

            #this statement checks to make sure 3 integers are entered into each lest
            #if not it a prompt is returned to user
            if (len(lst4)>3) or (len(lst5)>3) or (len(lst6)>3) or (len(lst1)>3) or (len(lst2)>3) or (len(lst3)>3):
                messagebox.showinfo("Error","Please enter maximum 3 integer values per matrix list")
            else:
                r = []
                result = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]
                if decider == "*":
                    for i in range(3):

                        for o in range(3):

                            for l in range(3):
                                result[i][o] += X[i][l] * Y[l][o]




                    for item in result:
                        r += item

                    input1 = "Multiplication of 2 matrix"

                    #function below uses numpy's array.reshape to create a new array which is 3 by 3
                    array = np.array(r)
                    newarray = array.reshape(1, 3, 3)
                    newarray = str(newarray)
                    self.format(newarray, 3, input1)

                #identifies if matrices are to be added
                #uses for loop to loop through values and then adds them up
                elif decider == "+":
                    for i in range(len(X)):

                        for z in range(len(X[0])):
                            result[i][z] = X[i][z] + Y[i][z]

                    for item in result:
                        r += item
                        array = np.array(r)
                    input1 = "Addition of 2 matrix"

                    #new array is created 3 by 3
                    newarray = array.reshape(1, 3, 3)
                    newarray = str(newarray)
                    self.format(newarray, 3, input1)

                # identifies if matrices are to be subtracted
                # uses for loop to loop through values and then subtracts them from each other
                elif decider == "-":
                    for i in range(len(X)):

                        for z in range(len(X[0])):
                            result[i][z] = X[i][z] - Y[i][z]

                    for item in result:
                        r += item
                    input1 = "Subtraction of 2 matrix"
                    array = np.array(r)
                    newarray = array.reshape(1, 3, 3)
                    newarray = str(newarray)
                    self.format(newarray, 3, input1)
                else:
                    #else statement if wrong operator entered it th ecalculator is not run
                    # but a prompt is returned to user
                    messagebox.showinfo("", "Please enter a operator from these three : + - * ")

        #try and except exception handling makes sure integer are entered
        except:
            messagebox.showinfo("", "Please enter a integer value")


    # carries out differentiation on expression entered
    #sympy function diff carries out differentiation on expression
    #exception handling where if incorrect expression entered user is informed
    def diff(self):
        x = Symbol('x')
        function = self.diffe.get()

        try:
            diff_final = str(diff(function, x))
            self.format(diff_final, 0, function)
        except:
            messagebox.showinfo("", "Please Enter Correct Details")

    #integrates expression using limits
    # sympy function integrate carries out integration on expression
    # exception handling where if incorrect expression entered user is informed
    def integlimits(self):
        x = Symbol('x')
        lim1 = (self.intelim1.get())
        lim2 = (self.intelim2.get())
        function = (self.inte.get())

        try:
            #limits are placed at the end of integrate function
            inte_final = str(integrate(function, (x, lim2, lim1)))
            self.answer_label(inte_final)
            type = "integration limits"


            #data to be inserted into complex calculations table for user
            s = "Limits are : "+str(lim1)+" and "+str(lim2)+" Function is: "+str(function)

            self.add_hist(inte_final, type, s)

        except:

            messagebox.showinfo("", "Please Enter Correct Details")

    # sympy integration function return integrated expression
    #expection handling in case wrong expression entered.
    def integ(self):
        x = Symbol('x')
        function = (self.inte.get())
        try:
            inte_final = str(integrate(function, x))
            self.format(inte_final, 1, function)

        except:
            messagebox.showinfo("", "Please Enter Correct Details")

    # formats the differentiated/integrated answers to look more presentable to user
    #also send relevant data to add_hist()
    #which inserts data into complex calculations table
    def format(self, func, type, entry):
        if type == 1:
            func = (func.replace("**", "^"))
            func = (func.replace("*", ""))
            self.answer_label(func)
            type = "integration"
            self.add_hist(func, type, entry)

        elif type == 3:
            func = (func.replace("[[", ""))
            func = (func.replace("]]", ""))
            func = (func.replace("[", ""))
            func = (func.replace("]", ""))
            self.answer_label(func)
            type = "matrix"
            self.add_hist(func, type, entry)

        else:
            func = (func.replace("**", "^"))
            func = (func.replace("*", ""))
            self.answer_label(func)
            type = "differentiation"
            self.add_hist(func, type, entry)

    #adds the corresponding data to the sql table by sending list with username to server
    def add_hist(self, answer, func, entry):

        #strftime function converts datetime into str so it can be sent over network
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        list=["COMPLEX INSERT",self.username,func,answer,entry,date]

        recieved=self.call.send(list)

    #when called this function runs the complex calculator window
    def run(self):
        self.window.mainloop()


# class for graphing calculations window
class graphingcalculations:
    def __init__(self, username):
        self.list = None
        self.axis_2 = None
        self.axis_1 = None
        self.call = client()
        self.username = username


    # fixes the tkinter window by sorting the rows and columns
    def window1(self):
        self.window = tk.Tk()
        self.window.geometry("700x500")
        self.window.title("Graphical calculations")
        self.window.wm_iconbitmap("calc.ico")
        self.window.configure(background="black")


        #sets up the tkinter window below

        self.framec()
        self.create_entry_buttons()

    #creates fram on window for widgets
    def framec(self):
        self.frame = Frame(self.window,width=600)
        self.frame.grid(row=0, column=0, ipadx=50)
        for i in range(0, 10):
            self.frame.grid_rowconfigure(i, weight=1)
        for i in range(0, 10):
            self.frame.grid_columnconfigure(i, weight=1)
        self.frame.configure(background="black")

    # creates labels and entries relevant to graphical calculations window
    #includes entries for equations and Axis ranges
    def create_entry_buttons(self):
        for i in range(10):
            for j in range(10):
                label = tk.Label(self.frame,bg="black")
                label.grid(row=i, column=j, padx=0, pady=0)

        self.label1 = tk.Label(self.frame, text="Create a graph for y=mx+c format", bg="black", fg="orange",font=norm)
        self.label1.grid(column=0, row=0)

        self.entry1 = tk.Entry(self.frame, bd=5, bg="white", fg="black", width=16, font=small_font)
        self.entry1.grid(column=1, row=3)

        self.entry2 = tk.Entry(self.frame, bd=5, bg="white", fg="black", width=16, font=small_font)
        self.entry2.grid(column=1, row=5)

        self.label2 = tk.Label(self.frame, text="Equation 1: y=", bg="black", fg="orange", font=norm)
        self.label2.grid(column=0, row=3)

        self.label3 = tk.Label(self.frame, text="Equation 2: y=", bg="black", fg="orange", font=norm)
        self.label3.grid(column=0, row=5)

        self.enter1 = tk.Button(self.frame, text="Enter", command=self.format, bg="black", fg="orange",height=2,width=10)
        self.enter1.grid(column=2, row=3, pady=0)

        self.enter1 = tk.Button(self.frame, text="History", command=self.checkhist, bg="black", fg="orange", height=2,width=10)
        self.enter1.grid(column=2, row=0, pady=0)

        self.labelaxis1 = tk.Label(self.frame, text="Axis range (X axis)", bg="black", fg="orange", font=norm)
        self.labelaxis1.grid(column=0, row=7)

        self.axis1 = tk.Entry(self.frame, bd=5, bg="white", fg="black", width=10, font=small_font)
        self.axis1.grid(column=0, row=8)

        self.labelaxis2 = tk.Label(self.frame, text="Axis range (Y axis)", bg="black", fg="orange", font=norm)
        self.labelaxis2.grid(column=1, row=7)

        self.axis2 = tk.Entry(self.frame, bd=5, bg="white", fg="black", width=10, font=small_font)
        self.axis2.grid(column=1, row=8)

    #runs the history window
    def checkhist(self):
        self.test = History(self.username)
        self.test.select_graph()
        self.test.gui_graph()

    # formats graph equations and axis as user desires
    def format(self):
        #axis is retrieved
        self.axis_1 = self.axis1.get()
        self.axis_2 = self.axis2.get()

        #if no axis entered default values used
        if (self.axis_1 or self.axis_2) == "":
            xrange = [-10, 10]
            yrange = [-10, 10]
            axis1="-10 10"
            axis2="-10 10"

        else:
            #if entered axis then range is worked out
            xrange = [int(x) for x in self.axis_1.split()]
            yrange = [int(x) for x in self.axis_2.split()]

        #excpetion handling to evaluate graph equations
        #outputs incorrect equation/axis if graph equation/axis not valid
        #work oyt graph points
        try:
            a = self.entry1.get()
            b = self.entry2.get()

            #used to set x axis range as shown by xrange[0] and xrange[1]
            #num suggests amount of points to be plotted
            x = np.linspace(xrange[0],xrange[1], num=1000)

            if a == "":
                orig1 = None
            else:
                orig1 = a
                a = eval(a)
            if b == "":
                orig2 = None
            else:
                orig2 = b
                b = eval(b)

            #sends evaluated equations to graph plotting function

            self.straight_linegraph(x,a, b, orig1, orig2,xrange,yrange)

            #valid graph data also sent off to be inserted into graphing table
            self.histadd(orig1, orig2, self.axis_1, self.axis_2, self.username)

        except:
            messagebox.showinfo("", "The Graph data is invalid please check your graph equations and check you have entered axis ranges in format eg: -10 10")

    #plots the graph again when clicked on in history window
    def graph_hist(self,equation1,equation2,axis1,axis2):
        xrange = [int(x) for x in axis1.split()]
        yrange = [int(x) for x in axis2.split()]

        x = np.linspace(xrange[0], xrange[1], num=1000)
        b=0
        a=0
        try:
            self.straight_linegraph(x, a, b, equation1, equation2, xrange, yrange)

        except:
            pass



    # function takes in graph data as parameters and plots it
    def straight_linegraph(self,x, a, b, equation1, equation2,xrang,yrang,):

        #loop to check which graph equation are entered and will plot those
        #if 1 graph equation entered that is plotted
        #if both graph equation entered both are sent to be plotted

        if equation1 is not None:
            if equation2 is not None:
                a=eval(equation1)
                b=eval(equation2)

                plt.plot(x, a, label=equation1)
                plt.plot(x, b, label=equation2)

            else:

                a=eval(equation1)
                plt.plot(x, a, label=equation1)

        #checks if other equation not empty it will plot the graph for equation 2
        elif equation2 is not None:

            b = eval(equation2)
            #plots the graph
            plt.plot(x, b, label=equation2)

        else:
            # prompt to let user know there were no equations entered
            messagebox.showinfo("", "You have not entered any graph equations")

        plt.xlim(*xrang)
        plt.ylim(*yrang)
        plt.grid(True)

        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#90FF33')

        plt.legend(loc='upper left')
        #shoows graph
        plt.show()

    #when valid graph plotted the graph data is sent to this function to be inserted
    #list is created to be senthrough client's sendlist() method to the server
    def histadd(self, equation1, equation2, axis1, axis2, username):
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.list=["GRAPHICAL INSERT",self.username,equation1,equation2,axis1,axis2,date]
        recieved=self.call.send(list)


    #runs the window
    def run(self):
        self.window1()
        self.window.mainloop()

#class for history window
class History:

    #stores attributes relevant for history window
    def __init__(self, username):
        self.eq2 = None
        self.eq1 = None
        self.axis2 = None
        self.axis1 = None
        self.equation2 = None
        self.equation1 = None
        self.call=client()

        self.grapheq1 = None
        self.row3 = None
        self.row2 = None
        self.row = None
        self.row1 = None
        self.username = username
        self.history = Tk()

    #selects details needed for graph gui by sending list with command "GRAPH HIST"
    #where the list sent should include username so result is returned for specific username
    #list recieved is then placed in rows for history window to access them
    def select_graph(self):
        list=["GRAPH HIST",self.username]

        recieved_list=self.call.send(list)
        self.row=recieved_list[0]
        self.row1=recieved_list[1]
        self.row2=recieved_list[2]
        self.row3=recieved_list[3]

    #shows the graph history gui with 10 labels for columns Equation 1
    #Equation 2 , Axis1 , Axis 2
    #also contains buttons next to each row of graph data
    #so graph can be plotted again
    def gui_graph(self):
        self.history.title("History")
        self.history.geometry("600x600")
        self.history.wm_iconbitmap("calc.ico")
        self.history.configure(background="black")
        for i in range(0, 10):
            self.history.rowconfigure(i, weight=1)
        for i in range(0, 10):
            self.history.columnconfigure(i, weight=1)

        l = tk.Label(self.history, text="Equation 1", bg="black", fg="white", padx=24, font=small_font)
        l.grid(column=0, row=0)

        label1 = tk.Label(self.history, text=self.row[0], bg="black", fg="white", padx=24, font=small_font)
        label1.grid(column=0, row=1)

        label2 = tk.Label(self.history, text=self.row[1], bg="black", fg="white", padx=24, font=small_font)
        label2.grid(column=0, row=2)

        label3 = tk.Label(self.history, text=self.row[2], bg="black", fg="white", padx=24, font=small_font)
        label3.grid(column=0, row=3)

        label4 = tk.Label(self.history, text=self.row[3], bg="black", fg="white", padx=24, font=small_font)
        label4.grid(column=0, row=4)

        label5 = tk.Label(self.history, text=self.row[4], bg="black", fg="white", padx=24, font=small_font)
        label5.grid(column=0, row=5)

        label6 = tk.Label(self.history, text=self.row[5], bg="black", fg="white", padx=24, font=small_font)
        label6.grid(column=0, row=6)

        label7 = tk.Label(self.history, text=self.row[6], bg="black", fg="white", padx=24, font=small_font)
        label7.grid(column=0, row=7)

        label8 = tk.Label(self.history, text=self.row[7], bg="black", fg="white", padx=24, font=small_font)
        label8.grid(column=0, row=8)

        label9 = tk.Label(self.history, text=self.row[8], bg="black", fg="white", padx=24, font=small_font)
        label9.grid(column=0, row=9)

        label10 = tk.Label(self.history, text=self.row[9], bg="black", fg="white", padx=24, font=small_font)
        label10.grid(column=0, row=10)

        l = tk.Label(self.history, text="Equation 2", bg="black", fg="white", padx=24, font=small_font)
        l.grid(column=2, row=0)

        label1 = tk.Label(self.history, text=self.row1[0], bg="black", fg="white", padx=24, font=small_font)
        label1.grid(column=2, row=1)

        label2 = tk.Label(self.history, text=self.row1[1], bg="black", fg="white", padx=24, font=small_font)
        label2.grid(column=2, row=2)

        label3 = tk.Label(self.history, text=self.row1[2], bg="black", fg="white", padx=24, font=small_font)
        label3.grid(column=2, row=3)

        label4 = tk.Label(self.history, text=self.row1[3], bg="black", fg="white", padx=24, font=small_font)
        label4.grid(column=2, row=4)

        label5 = tk.Label(self.history, text=self.row1[4], bg="black", fg="white", padx=24, font=small_font)
        label5.grid(column=2, row=5)

        label6 = tk.Label(self.history, text=self.row1[5], bg="black", fg="white", padx=24, font=small_font)
        label6.grid(column=2, row=6)

        label7 = tk.Label(self.history, text=self.row1[6], bg="black", fg="white", padx=24, font=small_font)
        label7.grid(column=2, row=7)

        label8 = tk.Label(self.history, text=self.row1[7], bg="black", fg="white", padx=24, font=small_font)
        label8.grid(column=2, row=8)

        label9 = tk.Label(self.history, text=self.row1[8], bg="black", fg="white", padx=24, font=small_font)
        label9.grid(column=2, row=9)

        label10 = tk.Label(self.history, text=self.row1[9], bg="black", fg="white", padx=24, font=small_font)
        label10.grid(column=2, row=10)

        l = tk.Label(self.history, text="Axis1", bg="black", fg="white", padx=24, font=small_font)
        l.grid(column=4, row=0)

        label1 = tk.Label(self.history, text=self.row2[0], bg="black", fg="white", padx=24, font=small_font)
        label1.grid(column=4, row=1)

        label2 = tk.Label(self.history, text=self.row2[1], bg="black", fg="white", padx=24, font=small_font)
        label2.grid(column=4, row=2)

        label3 = tk.Label(self.history, text=self.row2[2], bg="black", fg="white", padx=24, font=small_font)
        label3.grid(column=4, row=3)

        label4 = tk.Label(self.history, text=self.row2[3], bg="black", fg="white", padx=24, font=small_font)
        label4.grid(column=4, row=4)

        label5 = tk.Label(self.history, text=self.row2[4], bg="black", fg="white", padx=24, font=small_font)
        label5.grid(column=4, row=5)

        label6 = tk.Label(self.history, text=self.row2[5], bg="black", fg="white", padx=24, font=small_font)
        label6.grid(column=4, row=6)

        label7 = tk.Label(self.history, text=self.row2[6], bg="black", fg="white", padx=24, font=small_font)
        label7.grid(column=4, row=7)

        label8 = tk.Label(self.history, text=self.row2[7], bg="black", fg="white", padx=24, font=small_font)
        label8.grid(column=4, row=8)

        label9 = tk.Label(self.history, text=self.row2[8], bg="black", fg="white", padx=24, font=small_font)
        label9.grid(column=4, row=9)

        label10 = tk.Label(self.history, text=self.row2[9], bg="black", fg="white", padx=24, font=small_font)
        label10.grid(column=4, row=10)


        l = tk.Label(self.history, text="Axis2 ", bg="black", fg="white", padx=24, font=small_font)
        l.grid(column=6, row=0)

        label1 = tk.Label(self.history, text=self.row3[0], bg="black", fg="white", padx=24, font=small_font)
        label1.grid(column=6, row=1)

        label2 = tk.Label(self.history, text=self.row3[1], bg="black", fg="white", padx=24, font=small_font)
        label2.grid(column=6, row=2)

        label3 = tk.Label(self.history, text=self.row3[2], bg="black", fg="white", padx=24, font=small_font)
        label3.grid(column=6, row=3)

        label4 = tk.Label(self.history, text=self.row3[3], bg="black", fg="white", padx=24, font=small_font)
        label4.grid(column=6, row=4)

        label5 = tk.Label(self.history, text=self.row3[4], bg="black", fg="white", padx=24, font=small_font)
        label5.grid(column=6, row=5)

        label6 = tk.Label(self.history, text=self.row3[5], bg="black", fg="white", padx=24, font=small_font)
        label6.grid(column=6, row=6)

        label7 = tk.Label(self.history, text=self.row3[6], bg="black", fg="white", padx=24, font=small_font)
        label7.grid(column=6, row=7)

        label8 = tk.Label(self.history, text=self.row3[7], bg="black", fg="white", padx=24, font=small_font)
        label8.grid(column=6, row=8)

        label9 = tk.Label(self.history, text=self.row3[8], bg="black", fg="white", padx=24, font=small_font)
        label9.grid(column=6, row=9)

        label10 = tk.Label(self.history, text=self.row3[9], bg="black", fg="white", padx=24, font=small_font)
        label10.grid(column=6, row=10)

        button1 = tk.Button(self.history, text="Open graph", bg="black", fg="orange", height=1,width=8,command=lambda: self.graph(1))
        button1.grid(column=8, row=1, sticky=tk.W, padx=0)

        button2 = tk.Button(self.history, text="Open graph", command=lambda: self.graph(2), bg="black", fg="orange",height=1, width=8)
        button2.grid(column=8, row=2, sticky=tk.W, padx=0)

        button3 = tk.Button(self.history, text="Open graph", command=lambda: self.graph(3), bg="black", fg="orange",height=1, width=8)
        button3.grid(column=8, row=3, sticky=tk.W, padx=0)

        button4 = tk.Button(self.history, text="Open graph", command=lambda: self.graph(4), bg="black", fg="orange",height=1, width=8)
        button4.grid(column=8, row=4, sticky=tk.W, padx=0)

        button5 = tk.Button(self.history, text="Open graph", command=lambda: self.graph(5), bg="black", fg="orange",height=1, width=8)
        button5.grid(column=8, row=5, sticky=tk.W, padx=0)

        button6 = tk.Button(self.history, text="Open graph", command=lambda: self.graph(6), bg="black", fg="orange",height=1, width=8)
        button6.grid(column=8, row=6, sticky=tk.W, padx=0)

        button7 = tk.Button(self.history, text="Open graph", command=lambda: self.graph(7), bg="black", fg="orange",height=1, width=8)
        button7.grid(column=8, row=7, sticky=tk.W, padx=0)

        button8 = tk.Button(self.history, text="Open graph", command=lambda: self.graph(8), bg="black", fg="orange",height=1, width=8)
        button8.grid(column=8, row=8, sticky=tk.W, padx=0)

        button9 = tk.Button(self.history, text="Open graph", command=lambda: self.graph(9), bg="black", fg="orange",height=1, width=8)
        button9.grid(column=8, row=9, sticky=tk.W, padx=0)

        button10 = tk.Button(self.history, text="Open graph", command=lambda: self.graph(10), bg="black", fg="orange",height=1, width=8)
        button10.grid(column=8, row=10, sticky=tk.W, padx=0)

    #if the button for plotting graph is clicked this runs the command in the graphical class for graph to be plotted
    #using data which is retrieved from graphing calculations table
    def graph(self,k):
        k=k-1
        self.equation1=self.row[k]
        self.equation2=self.row1[k]
        self.eq1=self.equation1[0]
        self.eq2 = self.equation2[0]
        self.axis1=self.row2[k]
        self.axis2=self.row3[k]

        xaxis=self.axis1[0]
        yaxis=self.axis2[0]



        test=graphingcalculations(self.username)
        test.graph_hist(self.eq1,self.eq2,xaxis,yaxis)



    #plots the simple calculator history gui with correct columns
    def gui_simple(self):
        self.history.title("History")
        self.history.geometry("600x600")
        self.history.wm_iconbitmap("calc.ico")
        self.history.configure(background="black")
        for i in range(0, 10):
            self.history.rowconfigure(i, weight=1)
        for i in range(0, 7):
            self.history.columnconfigure(i, weight=1)

        l = tk.Label(self.history, text="Calculations", bg="black", fg="white", padx=24, font=small_font)
        l.grid(column=0, row=0)

        label1 = tk.Label(self.history, text=self.row[0], bg="black", fg="white", padx=24, font=small_font)
        label1.grid(column=0, row=1)

        label2 = tk.Label(self.history, text=self.row[1], bg="black", fg="white", padx=24, font=small_font)
        label2.grid(column=0, row=2)

        label3 = tk.Label(self.history, text=self.row[2], bg="black", fg="white", padx=24, font=small_font)
        label3.grid(column=0, row=3)

        label4 = tk.Label(self.history, text=self.row[3], bg="black", fg="white", padx=24, font=small_font)
        label4.grid(column=0, row=4)

        label5 = tk.Label(self.history, text=self.row[4], bg="black", fg="white", padx=24, font=small_font)
        label5.grid(column=0, row=5)

        label6 = tk.Label(self.history, text=self.row[5], bg="black", fg="white", padx=24, font=small_font)
        label6.grid(column=0, row=6)

        label7 = tk.Label(self.history, text=self.row[6], bg="black", fg="white", padx=24, font=small_font)
        label7.grid(column=0, row=7)

        label8 = tk.Label(self.history, text=self.row[7], bg="black", fg="white", padx=24, font=small_font)
        label8.grid(column=0, row=8)

        label9 = tk.Label(self.history, text=self.row[8], bg="black", fg="white", padx=24, font=small_font)
        label9.grid(column=0, row=9)

        label10 = tk.Label(self.history, text=self.row[9], bg="black", fg="white", padx=24, font=small_font)
        label10.grid(column=0, row=10)

        l = tk.Label(self.history, text="Answers", bg="black", fg="white", padx=24, font=small_font)
        l.grid(column=2, row=0)

        label1 = tk.Label(self.history, text=self.row1[0], bg="black", fg="white", padx=24, font=small_font)
        label1.grid(column=2, row=1)

        label2 = tk.Label(self.history, text=self.row1[1], bg="black", fg="white", padx=24, font=small_font)
        label2.grid(column=2, row=2)

        label3 = tk.Label(self.history, text=self.row1[2], bg="black", fg="white", padx=24, font=small_font)
        label3.grid(column=2, row=3)

        label4 = tk.Label(self.history, text=self.row1[3], bg="black", fg="white", padx=24, font=small_font)
        label4.grid(column=2, row=4)

        label5 = tk.Label(self.history, text=self.row1[4], bg="black", fg="white", padx=24, font=small_font)
        label5.grid(column=2, row=5)

        label6 = tk.Label(self.history, text=self.row1[5], bg="black", fg="white", padx=24, font=small_font)
        label6.grid(column=2, row=6)

        label7 = tk.Label(self.history, text=self.row1[6], bg="black", fg="white", padx=24, font=small_font)
        label7.grid(column=2, row=7)

        label8 = tk.Label(self.history, text=self.row1[7], bg="black", fg="white", padx=24, font=small_font)
        label8.grid(column=2, row=8)

        label9 = tk.Label(self.history, text=self.row1[8], bg="black", fg="white", padx=24, font=small_font)
        label9.grid(column=2, row=9)

        label10 = tk.Label(self.history, text=self.row1[9], bg="black", fg="white", padx=24, font=small_font)
        label10.grid(column=2, row=10)

        self.history.mainloop()

    #shows the complex gui history window with correct columns
    def gui_complex(self):
        self.history.title("History")
        self.history.geometry("800x800")
        self.history.wm_iconbitmap("calc.ico")
        self.history.configure(background="black")
        for i in range(0, 10):
            self.history.rowconfigure(i, weight=1)
        for i in range(0, 7):
            self.history.columnconfigure(i, weight=1)

        l = tk.Label(self.history, text="Inputs", bg="black", fg="white", padx=24, font=small_font)
        l.grid(column=0, row=0)

        label1 = tk.Label(self.history, text=self.row2[0], bg="black", fg="white", padx=24, font=small_font)
        label1.grid(column=0, row=1)

        label2 = tk.Label(self.history, text=self.row2[1], bg="black", fg="white", padx=24, font=small_font)
        label2.grid(column=0, row=2)

        label3 = tk.Label(self.history, text=self.row2[2], bg="black", fg="white", padx=24, font=small_font)
        label3.grid(column=0, row=3)

        label4 = tk.Label(self.history, text=self.row2[3], bg="black", fg="white", padx=24, font=small_font)
        label4.grid(column=0, row=4)

        label5 = tk.Label(self.history, text=self.row2[4], bg="black", fg="white", padx=24, font=small_font)
        label5.grid(column=0, row=5)

        label6 = tk.Label(self.history, text=self.row2[5], bg="black", fg="white", padx=24, font=small_font)
        label6.grid(column=0, row=6)

        label7 = tk.Label(self.history, text=self.row2[6], bg="black", fg="white", padx=24, font=small_font)
        label7.grid(column=0, row=7)

        label8 = tk.Label(self.history, text=self.row2[7], bg="black", fg="white", padx=24, font=small_font)
        label8.grid(column=0, row=8)

        label9 = tk.Label(self.history, text=self.row2[8], bg="black", fg="white", padx=24, font=small_font)
        label9.grid(column=0, row=9)

        label10 = tk.Label(self.history, text=self.row2[9], bg="black", fg="white", padx=24, font=small_font)
        label10.grid(column=0, row=10)

        l = tk.Label(self.history, text="Function done", bg="black", fg="white", padx=24, font=small_font)
        l.grid(column=4, row=0)

        label1 = tk.Label(self.history, text=self.row1[0], bg="black", fg="white", padx=24, font=small_font)
        label1.grid(column=4, row=1)

        label2 = tk.Label(self.history, text=self.row1[1], bg="black", fg="white", padx=24, font=small_font)
        label2.grid(column=4, row=2)

        label3 = tk.Label(self.history, text=self.row1[2], bg="black", fg="white", padx=24, font=small_font)
        label3.grid(column=4, row=3)

        label4 = tk.Label(self.history, text=self.row1[3], bg="black", fg="white", padx=24, font=small_font)
        label4.grid(column=4, row=4)

        label5 = tk.Label(self.history, text=self.row1[4], bg="black", fg="white", padx=24, font=small_font)
        label5.grid(column=4, row=5)

        label6 = tk.Label(self.history, text=self.row1[5], bg="black", fg="white", padx=24, font=small_font)
        label6.grid(column=4, row=6)

        label7 = tk.Label(self.history, text=self.row1[6], bg="black", fg="white", padx=24, font=small_font)
        label7.grid(column=4, row=7)

        label8 = tk.Label(self.history, text=self.row1[7], bg="black", fg="white", padx=24, font=small_font)
        label8.grid(column=4, row=8)

        label9 = tk.Label(self.history, text=self.row1[8], bg="black", fg="white", padx=24, font=small_font)
        label9.grid(column=4, row=9)

        label10 = tk.Label(self.history, text=self.row1[9], bg="black", fg="white", padx=24, font=small_font)
        label10.grid(column=4, row=10)



        l = tk.Label(self.history, text="Answers", bg="black", fg="white", padx=24, font=small_font)
        l.grid(column=2, row=0)

        label1 = tk.Label(self.history, text=self.row[0], bg="black", fg="white", padx=24, font=small_font)
        label1.grid(column=2, row=1)

        label2 = tk.Label(self.history, text=self.row[1], bg="black", fg="white", padx=24, font=small_font)
        label2.grid(column=2, row=2)

        label3 = tk.Label(self.history, text=self.row[2], bg="black", fg="white", padx=24, font=small_font)
        label3.grid(column=2, row=3)

        label4 = tk.Label(self.history, text=self.row[3], bg="black", fg="white", padx=24, font=small_font)
        label4.grid(column=2, row=4)

        label5 = tk.Label(self.history, text=self.row[4], bg="black", fg="white", padx=24, font=small_font)
        label5.grid(column=2, row=5)

        label6 = tk.Label(self.history, text=self.row[5], bg="black", fg="white", padx=24, font=small_font)
        label6.grid(column=2, row=6)

        label7 = tk.Label(self.history, text=self.row[6], bg="black", fg="white", padx=24, font=small_font)
        label7.grid(column=2, row=7)

        label8 = tk.Label(self.history, text=self.row[7], bg="black", fg="white", padx=24, font=small_font)
        label8.grid(column=2, row=8)

        label9 = tk.Label(self.history, text=self.row[8], bg="black", fg="white", padx=24, font=small_font)
        label9.grid(column=2, row=9)

        label10 = tk.Label(self.history, text=self.row[9], bg="black", fg="white", padx=24, font=small_font)
        label10.grid(column=2, row=10)


    #sql query for relevant complex history window
    def select_complex(self):
        list=["COMPLEX HIST",self.username]
        recieved_list=self.call.send(list)
        self.row=recieved_list[0]
        self.row1=recieved_list[1]
        self.row2=recieved_list[2]



    #sql for taking in relevant details for simple calculator
    def select_simple(self):
        list=["SIMPLE HIST",self.username]
        recieved_list=self.call.send(list)
        self.row=recieved_list[0]
        self.row1=recieved_list[1]
