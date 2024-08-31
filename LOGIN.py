#Imports Tkinter for the GUI while also importing mainmenu class to run window
#imports hashlib to hash password
from tkinter import *
from tkinter import messagebox
from client import *
import hashlib
from MAINMENU import mainmenu



#This class is responsible for sending login credentials to be authenticated
#This calss is also responsible inserting registration data into User table
class database:
    #stores attributes
    def __init__(self):

        self.profession1 = None
        self.password1 = None
        self.username1 = None
        self.age1 = None
        self.name1 = None
        self.call=client()



    #parameters in this function are login credentials
    #credentials checked by send data through client class to server
    def checklogin(self, username, password):
        list=["CHECK LOGIN",username,password]

        recieved_list=self.call.send(list)

        if username == "" and password == "":
            messagebox.showinfo("", "Nothing was entered")
        elif recieved_list[0]=="True":
            messagebox.showinfo("", "Correct", )
            return True
        else:
            messagebox.showinfo("Login Error", "Wrong details were entered ")

    # This function takes in username hashed password name age profession and therefore it sends the data in a list
    #to the server to be inserted
    def userdouble_check_create(self, name, age, username, password, profession):
        result = hashlib.sha384(password.encode())
        password = (result.hexdigest())
        list = ["CREATE ACCOUNT",name,age,username,password,profession]
        list_recieved=self.call.send(list)

        if list_recieved[0]=="Wrong":
            messagebox.showinfo("", "Wrong data type entered for age please enter a integer ")
        elif list_recieved[0]=="False":
            messagebox.showinfo("", "Username Taken please try a different username ")
        else:
            messagebox.showinfo("", "Account created, You may close this window")






# this class is for the login window
class loginpage(database):
    def __init__(self):
        super().__init__()
        # setup for tkinter window for the login system
        self.root = Tk()
        self.root.title("Login for the Calculator")
        self.root.geometry("950x650")
        self.root.wm_iconbitmap("calc.ico")
        self.root.configure(background="black")
        self.gui_widgets()

    # takes in login credentials and sends to database class
    #if returned True the mainmenu window is called and login page closed
    def login(self):
        username = self.usern.get()
        password = self.passw.get()
        result = hashlib.sha384(password.encode())
        password = (result.hexdigest())
        if self.checklogin(username, password) == True:
            self.root.destroy()
            ap = mainmenu(username)
            ap.run()
        else:
            pass


    # gui widgets are run for login page
    def gui_widgets(self):
        Label(self.root, text="Username", bg="black", fg="orange").place(x=350, y=200)
        Label(self.root, text="Password", bg="black", fg="orange").place(x=350, y=250)

        Button(self.root, text="Quit", command=self.close, height=2, width=20, bd=4, bg="black",
        fg="orange").place(x=800, y=0)

        self.usern = Entry(self.root, bd=5, bg="white", fg="black")
        self.usern.place(x=450, y=200)

        self.passw = Entry(self.root, bd=5, bg="white", fg="black", show="*")
        self.passw.place(x=450, y=250)

        Checkbox = Checkbutton(self.root, text="Show password", command=self.asterik, bg="Black",
        fg="White").place(x=600, y=250)

        Button(self.root, text="Login", command=self.login, height=2, width=17, bd=3, bg="black",
        fg="orange").place(x=450, y=300)

        Button(self.root, text="Create Account", command=self.registration, height=2, width=17,
        bd=4, bg="black",fg="orange").place(x=450, y=350)

    # Run to show/hide password
    def asterik(self):
        self.passw.config(show="")

    # runs the registration class/window
    def registration(self):
        reg = registration()
        reg.run()

    # closes this window and disconnects client from server
    def close(self):
        test=client()
        list=["DISCONNECT"]
        reply=test.send(list)
        self.root.destroy()

    # runs the login gui
    def runlog(self):
        self.root.mainloop()


# class dedicated to registration where it imports methods of database class
class registration(database):
    def __init__(self):
        super().__init__()
        self.setup = Tk()
        self.setup.title("Registration window")
        self.setup.geometry("500x500")
        self.setup.wm_iconbitmap("calc.ico")
        self.setup.configure(background="black")
        self.create_gui_widgets()

    # gui widgets are created for registration window and displayed when run
    def create_gui_widgets(self):
        for i in range(0, 10):
            self.setup.columnconfigure(i, weight=1)
            self.setup.rowconfigure(i, weight=1)

        name = (Label(self.setup, text="Name", bg="black", fg="orange"))
        name.grid(row=2, column=2)

        self.name1 = Entry(self.setup, bd=5, bg="black", fg="orange")
        self.name1.grid(row=2, column=3)

        age = Label(self.setup, text="Age in years", bg="black", fg="orange")
        age.grid(row=3, column=2)

        self.age1 = Entry(self.setup, bd=5, bg="black", fg="orange")
        self.age1.grid(row=3, column=3)

        username = Label(self.setup, text="Username", bg="black", fg="orange")
        username.grid(row=4, column=2)

        self.username1 = Entry(self.setup, bd=5, bg="black", fg="orange")
        self.username1.grid(row=4, column=3)

        password = Label(self.setup, text="Password", bg="black", fg="orange")
        password.grid(row=5, column=2)

        self.password1 = Entry(self.setup, bd=5, bg="black", fg="orange")
        self.password1.grid(row=5, column=3)

        profession = Label(self.setup, text="Profession", bg="black", fg="orange")
        profession.grid(row=6, column=2)

        self.profession1 = Entry(self.setup, bd=5, bg="black", fg="orange")
        self.profession1.grid(row=6, column=3)

        create = Button(self.setup, text="Create", command=self.usernamecheck, height=4,
        width=20, bd=4, bg="black",fg="orange")

        create.grid(row=3, column=4)

    # function to send registration details to database class method
    # which checks if username is taken and if not details are added to user table
    def usernamecheck(self):
        name = self.name1.get()
        age = self.age1.get()
        username = self.username1.get()
        password = self.password1.get()
        profession = self.profession1.get()
        self.userdouble_check_create(name, age, username, password, profession)

    #when called runs the registration window
    def run(self):
        self.setup.mainloop()


app = loginpage()
app.runlog()
