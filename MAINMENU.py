#Imports date time module, Tkinter library for GUI
#imports different calculation classes to run them when option selected
#imports client class to be able to send queries/statement and recieve reply from server
from datetime import datetime
from tkinter import *
from client import *
from MAIN import simplecalculator, complexcalculations, graphingcalculations

big_complexfont = ("Calibri", 12, "bold")
#class for main menu window.
class mainmenu:
   def __init__(self,username):
      #creates main menu tkinter window
      self.menu = Tk()
      self.call=client()
      self.menu.title("Main Menu")
      self.menu.geometry("750x500")
      self.menu.wm_iconbitmap("calc.ico")
      self.menu.configure(background="black")
      self.username=username
      self.Button = self.create_buttons()

   #creates option buttons for main menu
   def create_buttons(self):
      Button(self.menu,text="Simple Calculations", command= self.simplecalc,height=2,width =17,bd=3,bg="black",fg="orange").place(x=250,y=50)

      Button(self.menu,text="Complex Calculations", command= self.complexcalc,height=2,width =17,bd=3,bg="black",fg="orange").place(x=250,y=100)

      Button(self.menu,text="Graphing Calculations",command= self.graphcalc,height=2,width =17,bd=3,bg="black",fg="orange").place(x=250,y=150)

      Button(self.menu,text="Check Statistics",command=self.statistics,height=2,width=17, bd=3,bg="black",fg="orange").place(x=250, y=200)

      Button(self.menu,text="Exit", command=self.menu.destroy,height=2,width =17,bd=3,bg="black",fg="orange").place(x=250,y=250)

      return Button


   #runs main menu window
   def run(self):
      self.menu.mainloop()

   #runs the simple calc window up on click
   def simplecalc(self):

      calc = simplecalculator(self.username)
      calc.run()

   # runs the complex calc window up on click
   def complexcalc(self):

      calc= complexcalculations(self.username)
      calc.run()

   # runs the graphic calc window up on click
   def graphcalc(self):

      calc=graphingcalculations(self.username)
      calc.run()

   #this function is for displaying the statistics window
   #where different statistics are shown to user
   #sends queries to server to be carried out at desired table
   #receieves query results which is presented in the form of this window
   def statistics(self):
      self.stats = Tk()
      self.stats.title("Statistics")
      self.stats.geometry("500x500")
      self.stats.wm_iconbitmap("calc.ico")
      self.stats.configure(background="black")

      list = ["STATISTICS", self.username]
      list_recieved = self.call.send(list)

      number=list_recieved[0]
      number2=list_recieved[1]
      number3=list_recieved[2]
      number4=list_recieved[3]
      number5=list_recieved[4]
      number6=list_recieved[5]
      date = list_recieved[6]

      #converts datatype from string to datetime
      datemade = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

      current_time = datetime.now()

      time_difference = current_time - datemade

      days = time_difference.days

      hours, min_remainder = divmod(time_difference.seconds,3600)
      minutes, _ = divmod(min_remainder, 60)

      days_difference=days
      hours_difference = hours
      minutes_difference = minutes

      numb=number-10
      numb1=number2-10
      numb2=number3-10

      self.frame = Frame(self.stats)
      self.frame.grid(row=0,column=0)
      self.frame.configure(background="black")

      for i in range(0,10):
         self.frame.rowconfigure(i,weight=1)
         self.frame.columnconfigure(i,weight=1)

      name = (Label(self.frame, text="Username: "+self.username, bg="black", fg="orange",
      font=big_complexfont))

      name.grid(row=-0, column=0)

      numberof = (Label(self.frame, text="Number of simple calculations done: ", bg="black",fg="orange",font=big_complexfont))

      numberof.grid(row=3, column=0,ipady=10)

      numberof1 = (Label(self.frame, text=numb, bg="black", fg="orange",font=big_complexfont))

      numberof1.grid(row=3, column=1)

      numberof2 = (Label(self.frame, text="Number of graphical calculations done: ", bg="black",fg="orange",font=big_complexfont))

      numberof2.grid(row=5, column=0,ipady=10)

      numberof3 = (Label(self.frame, text=numb1, bg="black", fg="orange",font=big_complexfont))
      numberof3.grid(row=5, column=1)

      numberof4 = (Label(self.frame, text="Number of complex calculations done: ", bg="black",
      fg="orange",font=big_complexfont))

      numberof4.grid(row=7, column=0,ipady=10)

      numberof4 = (Label(self.frame, text=numb2, bg="black", fg="orange",font=big_complexfont))
      numberof4.grid(row=7, column=1)

      dateofreg = (Label(self.frame, text="You created your account: "+str(days_difference)+" days"
      " and "+str(hours_difference)+" hours and "+str(minutes_difference)+" minutes ago" ,
      bg="black", fg="orange", font=big_complexfont))

      dateofreg.grid(row=9, column=0)
      avg = (Label(self.frame, text="Average simple calculator answer: "+str(number4),bg="black", fg="orange", font=big_complexfont))

      avg.grid(row=10, column=0, ipady=10)

      max = (Label(self.frame, text="Maximum simple calculator answer: " + str(number5),bg="black", fg="orange",font=big_complexfont))

      max.grid(row=11, column=0, ipady=10)

      min = (Label(self.frame, text="Maximum simple calculator answer: " + str(number6),bg="black", fg="orange",font=big_complexfont))

      min.grid(row=12, column=0, ipady=10)


