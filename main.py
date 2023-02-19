import csv
class Person:
    def __init__(self):
         self._name = None
         self._email = None
         self._phoneno = None
    def getinfo(self):
        self._name = input("Please enter your name: ")
        self._email = input("Please enter your email: ")
        self._phoneno = input("Please enter your phone no: ")
    def register(self):
        with open("register.csv",'w+',newline="") as f:
            w =  csv.writer(f)
            self.username = input("Enter and set username      :")
            self.password = input("Enter and set your password :")
            w.writerow([self.username,self.password])
            print("Registration successfully")
            pass
    def login(self):
        my_lst=[] 
        with open("register.csv",'r+',newline="") as f:
            r =  csv.reader(f)
            data = list(r)
            for i in data:
                for j in i:
                    my_lst.append(j)
        while (True):
            self.username= input("Please Enter your username:  ")
            self.password= input("Please Enter the password: ")
            if self.username == str(my_lst[0]) and self.password == str(my_lst[1]):
                print()
                print("Login successfully")
                break
            else:
                print("Enter correct username and password ")
            print()
        print("********Welcome to Daewoo Bus Portal*********")
class Admin(Person):#Inheritance
    def login(self):
        super().login()
        print("Welcome to Admin")
    def bookedseats(self):
        with open("passenger.csv") as f:
           reader = csv.reader(f)
           for row in reader:
               print(' '.join(row) )
    def Displaypayment(self, paymentobj):
        paymentobj.display()
    def Feedbackview(self,feedbackobj):
        feedbackobj.display()
class Booking: 
    def __init__(self):
        self.seatno = None
    def seat(self):
        print(" |1|* |2|*|3|* |4|* |5|* |6|* |7|* |8|* |9| *|10|*|11|*|12|*")
        print("|13|*|14|*|15|*|16|*|17|*|18|*|19|*|20|*|21|*|22|*|23|*|24|*")
        print("|25|*|26|*|27|*|28|*|29|*|30|*|31|*|32|*|33|*|34|*|35|*|36|*")
        seatNoList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        self.bookingList=[]
        while True:
            self.seatno = int(input("Choose a Seat Number you want to book :"))
            if self.seatno<=30:
                
                if  self.seatno in seatNoList:
                    self.bookingList.append(self.seatno)
                    del seatNoList[self.seatno+1]
                    count = len(seatNoList)
                else:
                    print("Ticket Allready Booked")
                print("Do You Want To Book One More Seat Enter (y/n)") 
                y = input("") 
                if y == "y":
                    pass
                else:
                    break
            else:
                print("Don't Choose a Seat Number Which is Not Available")    
    def Display(self):
        return self.seatno
class Vehicle:
    def __init__(self):
        self.noofpassenger = None
        self.type =None
        self.price = None
    def businfo(self):
        self.noofpassenger = int(input("Enter the no of passenger: "))        
        print(" 1. Business BUS     = 1500 Fare")
        print(" 2. Executive BUS    = 800 Fare")
        self.busType = int(input("Select Bus Type  :"))
        if self.busType == 1:
            self.type = "Business BUS"
            self.price = self.noofpassenger*1500
        elif self.busType == 2:
            self.type = "Executive BUS"
            self.price = self.noofpassenger*800
    def Display(self):
        return self.type
        return self.price
        
class Passenger(Person): #Inheritance
    def __init__(self):
        super().__init__()
        self.departureLocation = None
        self.arivalLocation = None
        self.date = None
        self.seatno = None
        self.time = None
        self.autoInc = 1
        self.countcol= 0
    def GetPassengerinfo(self):
        Person.__init__(self)
        super().getinfo()
        print("1: Lahore")
        self.userinput1 = int(input("Enter Departure Location: "))
        if self.userinput1 == 1:
            self.departureLocation = "Lahore"
        else:
            print("Please Enter correct choice : ")
        print("1: Karachi")
        print("2: Multan")
        print("3: Faislabad")
        print("4: Islamabad")
        self.userinput2 = int(input("Enter Destination Location  :"))
        if self.userinput2 == 1:
            self.arivalLocation = "Karachi"
        elif self.userinput2 == 2:
            self.arivalLocation = "Multan"
        elif self.userinput2 == 3:
            self.arivalLocation = "Faislabad"
        elif self.userinput2 == 4:
            self.arivalLocation = "Islamabad"
        self.date = input("Enter the date in this Format: 18-02-22 :  ")
        print("Seclect the time: \n 1: 11:00am \n 2: 2:00pm \n 3: 6:00pm")
        userinput3 = int(input("Please enter the correct choice: "))
        if userinput3 ==1:
            self.time = "11:00am"
        elif userinput3 ==2:
            self.time ="2:00pm"
        elif userinput3 == 3:
            self.time = "6:00pm"
        #Composition
        self.bookingobj = Booking()
        self.vehicleobj = Vehicle()
        self.vehicleobj.businfo()
        self.bookingobj. seat()

    def saveInfo(self):
        self.autoInc = 1
        self.countcol= 0
        try:
            with open("passenger.csv",'r+',newline="") as f:
                r =  csv.reader(f)
                data = list(r)
                for  i in data:
                    self.autoInc += 1
                    for j in i:
                        self.countcol +=1
                    print()
                print("Number of Records Are Found In Database :",self.autoInc)                
        except:
            print("Your data is saved without record")
        finally:     
            with open("passenger.csv",'a+',newline="\n") as f:
                w =  csv.writer(f)
                w.writerow([self.autoInc,self._name,self._email, self._phoneno,self.departureLocation,self.arivalLocation,self.date,self.bookingobj.seatno,self.vehicleobj.noofpassenger,self.vehicleobj.type,self.vehicleobj.price,self.time])
                print("Data Save successfully")
                print()
class Ticket:
    def Displayreciept(self):
        my_lst = [] 
        with open("passenger.csv",'r+',newline="") as f:
            r =  csv.reader(f)
            data = list(r)
            id = int(input("Enter Your Booking Id  :"))
            for i in data:
                if id == int(i[0]):
                    for j in i:
                        my_lst.append(j)
                    break
        print("------------------------------------------------------------------------------")
        print("                 *********Daewoo Bus Ticket System*********                   ")
        print("------------------------------------------------------------------------------")
        print()
        print(" Online Ticket :", "Station 1        : Daewoo Bus Stand, Thokhar Niaz Baig    ")
        print("                             Ticket no",my_lst[0],".00                        ")
        print()
        print("Name: ",my_lst[1],"         Email: ",my_lst[2],"          Phone No: ",my_lst[3])
        print()
        print("______________________________________________________________________________")
        print()
        print(" Date of Booking :",my_lst[6],"  Time: ",my_lst[11] ,"Seat No :",my_lst[7],    )
        print()
        print("Departure Location:  ",my_lst[4],"           Destination:  ",my_lst[5]         )
        print(" Bus Type :       ",my_lst[9],"                                               ")
        print(" Bus Fare :       ",my_lst[10],"                                              ")
        print()
        print("------------------------------------------------------------------------------")
                
class Feedback:
    def __init__(self):
        self.message = None
    def getinfo(self):
        print("Enter any complaint or suggestion")
        self.message = str(input("Enter your meassage:  "))
        print("Thank you for your response")
        infile = open("feedback.txt", "a+")
        my_str = self.message +" " 
        infile.write(my_str)
        infile.close()
    def display(self):
        with open("feedback.txt", "r") as f:
            data = f.readlines()
            print(data)
class Payment:
    def __init__(self):
        self.totalsum = None
    def totalpayment(self):
        filename = open('passenger.csv', 'r')
        file = csv.DictReader(filename)
        price = []
        for col in file:
            price.append(col['price'])
        x= price
        test_list = x
        for i in range(0, len(x)):
            x[i] = int(x[i])
            intlst = x
        total = 0
        for ele in range(0, len(x)):
            total = total + x[ele]
            self.totalsum = total
    def display(self):
        print("The Total Sum of Passenger is: ",self.totalsum)
        
def main():
    print("1. Passenger Registration :")
    print("2. Passenger login        :")
    print("3. Admin login         :")
    personobj = Person()
    ch = int(input("Choose Correct option :"))
    if ch == 1:
        personobj.register()
        print("Enter the information to login: ")
        personobj.login()
        print()
        print("1. For info and buy ticket :")
        print("2. Show Ticket            :")
        print("3.Feedback")
        ch = int(input("Choose Any One Option :"))
        if ch == 1:
            bookingobj = Passenger()
            bookingobj.GetPassengerinfo()
            bookingobj.saveInfo()
            print("Press 1 to print the ticket: ")
        user_input = int(input("Enter your choice: "))
        if user_input ==1:
            ticketobj = Ticket()
            ticketobj.Displayreciept()                
        elif ch ==2:
            ticketobj = Ticket()
            ticketobj.Displayreciept()
        elif ch == 3:
            feedbackobj = Feedback()
            feedbackobj.getinfo()
            print("Thank you, Your response is noted")
    if ch == 2:
        personobj.login()
        print()
        print("1. For info and buy ticket ")
        print("2. Show Ticket            ")
        print("3.Feedback")
        ch = int(input("Choose Any One Option :"))
        if ch == 1:
            bookingobj = Passenger()
            bookingobj.GetPassengerinfo()
            bookingobj.saveInfo()
            print("Press 1 to print the ticket: ")
            user_input = int(input("Enter your choice: "))
            if user_input ==1:
            
                ticketobj = Ticket()
                ticketobj.Displayreciept()
                print("Press 1 to Give feedbcak or complaint\nPress 2 to close")
                input1 = int(input("Enter your response: "))
                if input1 ==1:
                    feedbackobj = Feedback()
                    feedbackobj.getinfo()
                if input1 ==2:
                    print(         "******Thank You For Using Daewoo Services******")
                    print()
                    print(               "               Safe Travel         ")           
        elif ch ==2:
            ticketobj = Ticket()
            ticketobj.Displayreciept()
        elif ch == 3:#Polymorphism
            feedbackobj = Feedback()
            feedbackobj.getinfo()
            print("Thank you, Your response is noted")
            print(         "******Thank You For Using Daewoo Services******")
            print()
            print(           "               Safe Travel         ")

    if ch == 3:
        adminobj = Admin()
        adminobj.login()
        print(" Press 1 to print the details of passenger, \n press 2 to see the total amount /n Press 3 to see the feedback of passengers : ")
        userinput = int(input("Enter your choice: "))
        if userinput == 1:
            adminobj.bookedseats()
            print("For payment details press 1: ")
            input3 = int(input("Enter your choice: "))
            if input3 == 1:
                paymentobj = Payment()
                paymentobj.totalpayment()
                adminobj.Displaypayment(paymentobj)
        if userinput == 2:
            #Association
            paymentobj = Payment()
            paymentobj.totalpayment()
            adminobj.Displaypayment(paymentobj)
        if userinput == 3:  #Polymorphism
            feedbackobj = Feedback()
            feedbackobj.display()
main()
            
        
