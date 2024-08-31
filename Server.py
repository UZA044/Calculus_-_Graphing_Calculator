#imports socket to host server
#imports threading to allow multiple clients to connecting
#json is imported to convert list into string so it can be sent over network
#imports my sql connector so that it is able to connect o my sql database
import socket
import threading
import json
import mysql
import mysql.connector
from datetime import datetime


#SERVER class used to host server for clients to connect to
class server:
    #stores attributes necessary for hosting server example : PORT AND IP address
    def __init__(self):
        self.connection = None
        self.PORT = 5030
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = (self.SERVER, self.PORT)
        self.server.bind(self.address)
        self.list_from_client=None


        #used to connect to SQL table
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password123",
            database="mydatabase"
        )

    # This function starts the server and it uses a while loop to listen for any connections
    #and when this occurs it creates a thread for new connection so simultaneous queries can occur
    def start_serv(self):

        self.server.listen(10)
        print(f"[LISTENING ON] {self.SERVER} ")
        while True:
            self.connection ,self.address= self.server.accept()
            client_thread = threading.Thread(target=self.handler, args=(self.connection, self.address))
            client_thread.start()

    #this function recieved the list from client and handles any queries / commands by
    #by sending list to desired function
    def handler(self,connection,address):

        print(f"[NEW CONNECTION] {address} connected.")
        message = connection.recv(8024).decode()



        self.list_from_client = json.loads(message)
        print(f"Received list from {address}: {self.list_from_client}")



        if self.list_from_client[0]=="SIMPLE HIST":
            self.simple_hist(self.list_from_client)

        elif self.list_from_client[0]=="SIMPLE INSERT":
            self.simple_calc_insert(self.list_from_client)

        elif self.list_from_client[0]=="CHECK LOGIN":
            self.logincheck(self.list_from_client)

        elif self.list_from_client[0]=="DISCONNECT":
            self.disconnect()
            print(f"[DISCONNECTING]{self.address}")

        elif self.list_from_client[0]=="CREATE ACCOUNT":
            self.user_double_check(self.list_from_client)

        elif self.list_from_client[0]=="STATISTICS":
            self.statistics(self.list_from_client)

        elif self.list_from_client[0]=="COMPLEX INSERT":
            self.complex_insert(self.list_from_client)

        elif self.list_from_client[0]=="GRAPHICAL INSERT":
            self.graphical_insert(self.list_from_client)

        elif self.list_from_client[0]=="GRAPH HIST":
            self.graph_hist(self.list_from_client)

        elif self.list_from_client[0]=="COMPLEX HIST":
            self.complex_hist(self.list_from_client)

        else:
            print("not working")

    #disconnects client from server
    def disconnect(self):
        list=["DISCONNECTING"]
        self.send_list(list)
        self.connection.close()
        print(f"[ACTIVE CONNECTION] {threading.activeCount() - 1}")

    #this function is called when the client connects to the server and needs to authenticate login credentials
    #hence the sql query is carried out and reply list is made according to authentication
    def logincheck(self,list):
        username=list[1]
        password=list[2]


        mycursor = self.mydb.cursor()
        sql = "SELECT * FROM User where BINARY username ='%s' AND BINARY password ='%s'" % (username, password)
        mycursor.execute(sql)
        if mycursor.fetchone():
            reply = ["True"]
            self.send_list(reply)

        else:
            reply = ["False"]
            self.send_list(reply)

    #this function selects calculations and answers from User Table for a specific user and places this in a list
    #ready to be sent back
    def simple_hist(self,list):
        username=list[1]

        mycursor = self.mydb.cursor()
        mycursor.execute(
            "SELECT calculation FROM calculations where username ='%s' ORDER BY created DESC" % (username))

        row = mycursor.fetchall()


        mycursor.execute("SELECT answer FROM calculations where username ='%s' ORDER BY created DESC" % (username))

        row1 = mycursor.fetchall()
        reply=[row,row1]
        self.send_list(reply)

    #this function is run to insert data sent from client in form of list into the user table but first
    #the sql statement is run to check of username is taken or not
    def user_double_check(self,list):
        username=list[3]
        mycursor = self.mydb.cursor()
        sql1 = "SELECT * FROM User where BINARY username ='%s'" % (username)
        mycursor.execute(sql1)

        if mycursor.fetchone():
            reply=["False"]
            self.send_list(reply)
        else:
            reply=["True"]
            self.create_new_account(list)

    #this function is used to insert data after authentication that username is not taken into the user table
    #for the registration process
    def create_new_account(self,list):
        name=list[1]
        age=list[2]
        username=list[3]
        password=list[4]
        profession=list[5]
        mycursor = self.mydb.cursor()


        try:
            mycursor.execute("INSERT INTO User (name,age,username,password,profesion) VALUES (%s,%s,%s,%s,%s)",
                         (name, age, username, password, profession))
            self.mydb.commit()
            self.insert_new_account(list)
        except:
            reply=["Wrong"]
            self.send_list(reply)

     #This function is run when a new account has been created and hence Graphical calculations, complex calculations,
     #simple_calculations are also inserted with values 0 for any calculation/answer data to make sure history window
    #does not crash as on new account there will be no data for history windows to display
    def insert_new_account(self,list):
        name = list[1]
        age = list[2]
        username = list[3]
        password = list[4]
        profession = list[5]

        mycursor = self.mydb.cursor()
        for i in range(0, 10):
            mycursor.execute("INSERT INTO Calculations (username,calculation,answer,created) VALUES (%s,%s,%s,%s)",
                             (username, 0, 0, datetime.now()))
        self.mydb.commit()

        for i in range(0, 10):
            mycursor.execute(
                "INSERT INTO complex_calculations (username,func,answer,created,input) VALUES (%s,%s,%s,%s,%s)",
                (username, 0, 0, datetime.now(), 0))
        self.mydb.commit()

        for i in range(0, 10):
            mycursor.execute(
                "INSERT INTO graphical_calculations (username,equation1,equation2,AXIS1,AXIS2,created) VALUES (%s,%s,%s,%s,%s,%s)",
                (username, 0, 0, 0, 0, datetime.now()))
        self.mydb.commit()

        listr=["True"]
        self.send_list(listr)

    #function is run to insert calculations and answer for simple calculator per user
    def simple_calc_insert(self,list):
        username=list[1]
        calculation=list[2]
        answer=list[3]
        created=list[4]
        date = datetime.strptime(created, '%Y-%m-%d %H:%M:%S')

        mycursor = self.mydb.cursor()
        mycursor.execute("INSERT INTO calculations (username,calculation,answer,created) VALUES (%s,%s,%s,%s)",
                         (username, calculation, answer, date))

        self.mydb.commit()
        reply=["TRUE"]
        self.send_list(reply)

    #this function is run to select all relevant data to be displayed on statistics window
    def statistics(self,list):
        username=list[1]
        mycursor = self.mydb.cursor(buffered=True)

        sql = "SELECT count(calculation) FROM calculations where BINARY username ='%s'" % (username)
        mycursor.execute(sql)
        number = mycursor.fetchone()

        sql1 = "SELECT count(equation1) FROM graphical_calculations where BINARY username ='%s'" % (username)
        mycursor.execute(sql1)
        number2 = mycursor.fetchone()

        sql2 = "SELECT count(answer) FROM complex_calculations where BINARY username ='%s'" % (username)
        mycursor.execute(sql2)
        number3 = mycursor.fetchone()

        innerjoin = "Select complex_calculations.created FROM complex_calculations INNER JOIN graphical_calculations ON " \
                    "graphical_calculations.username = complex_calculations.username INNER JOIN calculations ON " \
                    "calculations.username = graphical_calculations.username WHERE complex_calculations.username ='%s' " \
                    % (username)

        mycursor.execute(innerjoin)
        datecreated = (mycursor.fetchone())
        date = datecreated[0].strftime('%Y-%m-%d %H:%M:%S')

        sql3 = "SELECT AVG(answer) FROM calculations where BINARY username ='%s'" % (username)
        mycursor.execute(sql3)
        number4 = mycursor.fetchone()

        sql4 = "SELECT MIN(answer) FROM calculations where BINARY username ='%s'" % (username)
        mycursor.execute(sql4)
        number5 = mycursor.fetchone()

        sql5 = "SELECT MAX(answer) FROM calculations where BINARY username ='%s'" % (username)
        mycursor.execute(sql5)
        number6 = mycursor.fetchone()


        reply=[number[0],number2[0],number3[0],number4[0],number5[0],number6[0],date]
        self.send_list(reply)

    # function is run to insert input,function type  and answer for complex calculator per user
    def complex_insert(self,list):
        username=list[1]
        func=list[2]
        answer=list[3]
        input=list[4]
        created = list[5]
        date = datetime.strptime(created, '%Y-%m-%d %H:%M:%S')

        mycursor = self.mydb.cursor()

        mycursor.execute(
            "INSERT INTO complex_calculations (username,func,answer,input,created) VALUES (%s,%s,%s,%s,%s)",
            (username, func, answer, input, date))

        self.mydb.commit()
        reply=["TRUE"]
        self.send_list(reply)

    #function is run to insert graphical data recieved from client into graphical calculations table per user
    def graphical_insert(self,list):
        username=list[1]
        equation1=list[2]
        equation2=list[3]
        axis1=list[4]
        axis2=list[5]
        created = list[6]
        date = datetime.strptime(created, '%Y-%m-%d %H:%M:%S')

        mycursor = self.mydb.cursor()

        mycursor.execute(
            "INSERT INTO graphical_calculations (username,equation1,equation2,axis1,axis2,created) VALUES (%s,%s,%s,%s,%s,%s)",
            (username, equation1, equation2, axis1, axis2, date))

        self.mydb.commit()
        reply=["TRUE"]
        self.send_list(reply)

    # this function is run to select all relevant data to be displayed on complex calculator history window
    def complex_hist(self,list):
        username=list[1]
        mycursor = self.mydb.cursor()

        mycursor.execute(
            "SELECT answer FROM complex_calculations where username ='%s' ORDER BY created DESC" % (username))

        row = mycursor.fetchall()

        mycursor.execute(
            "SELECT func FROM complex_calculations where username ='%s' ORDER BY created DESC" % (username))

        row1 = mycursor.fetchall()

        mycursor.execute(
            "SELECT input FROM complex_calculations where username ='%s' ORDER BY created DESC" % (username))

        row2 = mycursor.fetchall()
        reply=[row,row1,row2]
        self.send_list(reply)

    # this function is run to select all relevant data to be displayed on graphical history window
    def graph_hist(self,list):
        username=list[1]
        mycursor = self.mydb.cursor()

        mycursor.execute(
            "SELECT equation1 FROM graphical_calculations where username ='%s' ORDER BY created DESC" % (username))

        row = mycursor.fetchall()

        mycursor.execute(
            "SELECT equation2 FROM graphical_calculations where username ='%s' ORDER BY created DESC" % (username))

        row1 = mycursor.fetchall()

        mycursor.execute(
            "SELECT AXIS1 FROM graphical_calculations where username ='%s' ORDER BY created DESC" % (username))

        row2 = mycursor.fetchall()

        mycursor.execute(
            "SELECT AXIS2 FROM graphical_calculations where username ='%s' ORDER BY created DESC" % (username))

        row3 = mycursor.fetchall()
        reply=[row,row1,row2,row3]
        self.send_list(reply)

    #this function is used to send back list that has data from server which was asked from client
    #this sends it by encoding and then sent to IP an dport it connected from
    #the thread and connection is then closed
    def send_list(self,reply):
        sendback=json.dumps(reply)
        self.connection.sendall(sendback.encode())
        self.connection.close()


test=server()
test.start_serv()




