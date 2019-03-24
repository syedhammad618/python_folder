class airline:
    def __init__(self,seat1,seat2,seat3,seat4):
        self.seat1=seat1
        self.seat2=seat2
        self.seat3=seat3
        self.seat4=seat4
    def customer(self):
         print("1 For Ticket Reservation.\n ")
         print("2 For Display Seat.\n")
         print("3 For Delete.\n")
         print("4 For Search.\n")
         print("5 For Number Of Seats.\n")
         print("6 For Log Out.\n")
class ticket(airline):
    def __int__(self):
        airline.__init__(self,seat1,seat2,seat3,seat4)
    def customers(self):
            while 1:
                tic=int(input("Enter The Number To Choose The Options: "))
                if tic==1:
                    cus=str(input("Enter The Name Who Booked The Ticket: "))
                    seat=int(input("Enter The Number Of Seats Will Be Booked: "))
                    buss=str(input("Enter The Class Of Airline: "))
                    if buss==business:
                        if self.seat1<=50:
                            f=open("business.txt","a+")
                            for i in range(seat):
                                cuss=str(input("Enter The Name Of Traveler: "))
                                f.write("Name:"+cuss)
                                f.write("\n")
                                age=input("Enter The Age Of Traveler: ")
                                f.write("Age:"+age)
                                f.write("\n")
                                book=input("Enter The Destination Do You Want To Go: ")
                                f.write("Destination:"+book)
                                f.write("\n")
                                f.write("Price:"+"Rs 250000")
                                f.write("\n")
                                self.seat1=self.seat1+1
                            f.close()
                            f=open("seat1.txt","w")
                            self.seat3 = self.seat3 - seat
                            self.seat3=str(self.seat3)
                            f.write(self.seat3)
                            f.close()
                        if self.seat1>50:
                            print("There Is No More Seat In Business Class.")
                    if buss==economy:
                        if self.seat2<=50:
                            f=open("economy.txt","a+")
                            for j in range(seat):
                                cuss=str(input("Enter The Name Of Traveler: "))
                                f.write("Name:"+cuss)
                                f.write("\n")
                                age=input("Enter The Age Of Traveler: ")
                                f.write("Age:"+age)
                                f.write("\n")
                                book = input("Enter The Destination Do You Want To Go: ")
                                f.write("Destination:" + book)
                                f.write("\n")
                                f.write("Price:"+"Rs 250000")
                                f.write("\n")
                                self.seat2=self.seat2+1
                            f.close()
                            f = open("seat2.txt", "w")
                            self.seat4 = self.seat4 - seat
                            self.seat4 = str(self.seat4)
                            f.write(self.seat4)
                            f.close()
                        if self.seat2>50:
                            print("There Is No More Seat In Economy Class.")
                if tic==2:
                    dis=input("Enter The Class Of Airline You Want To Display: ")
                    if dis==business:
                        file=open("business.txt","r+")
                        print (file.read())
                        file.close()
                    if dis==economy:
                        file = open("economy.txt", "r+")
                        print(file.read())
                        file.close()
                if tic==3:
                    blue = input("Enter The Name You Want To Delete: ")
                    buss1=input("Enter The Class Of Airline: ")
                    if buss1==business:
                        f = open("seat1.txt", "r")
                        self.seat3=f.readline()
                        self.seat3=int(self.seat3)
                        f.close()
                        f=open("seat1.txt","w")
                        self.seat3=int(self.seat3)+1
                        self.seat3=str(self.seat3)
                        f.write(self.seat3)
                        f.close()
                        with open("business.txt","r") as f:
                            data=f.readlines()
                            for i in data:
                                list.append(i)
                        for j in list:
                            if j==("Name:"+blue+"\n"):
                                c=list.index(j)
                                del list[c:c+4]
                                break

                        #print(list)
                        f.close()
                        file=open("business.txt","w")
                        for i in list:
                            file.write(i)
                        file.close()
                    if buss1==economy:
                        f = open("seat2.txt", "r")
                        self.seat4 = f.readline()
                        self.seat4 = int(self.seat4)
                        f.close()
                        f = open("seat2.txt", "w")
                        self.seat4 = int(self.seat4) + 1
                        self.seat4 = str(self.seat4)
                        f.write(self.seat4)
                        f.close()
                        with open("economy.txt","r") as f:
                            data1=f.readlines()
                            for j in data1:
                                list1.append(j)
                        for j in list1:
                            if j==("Name:"+blue+"\n"):
                                c=list1.index(j)
                                del list1[c:c+4]
                                break

                        #print(list1)
                        f.close()
                        file=open("economy.txt","w")
                        for j in list1:
                            file.write(j)
                        file.close()
                if tic==4:
                    cred1=input("Enter The Name You Want To Search: ")
                    cred=input("Enter The Class Of Airline: ")
                    if cred==business:
                        file=open("business.txt","r")
                        data2=file.readlines()
                        for k in data2:
                            if k==("Name:"+cred1+"\n"):
                                print(k+" is traveling in Business Class.")
                        file.close()
                    if cred==economy:
                        file=open("economy.txt","r")
                        data3=file.readlines()
                        for l in data3:
                            if l==("Name:"+cred1+"\n"):
                                print(l+" is traveling in Economy Class.")
                        file.close()
                if tic==5:
                    buss3=input("Enter The Class Of Airline: ")
                    if business==buss3:
                        f=open("seat1.txt","r")
                        print(f.read())
                        f.close()
                    if buss3==economy:
                        f=open("seat2.txt","r")
                        print(f.read())
                        f.close()
                if tic==6:
                    print("SYSTEM WAS LOGOUT!!!!")
                    break




name=str("Airline")
passw="password"
business = "business"
economy = "economy"
seat1=0
seat2=0
seat3=50
seat4=50
list=[]
data3=[]
list1=[]
username=str(input("Enter The Username: "))
if name==username:
    password=input("Enter Your Password: ")
    if password==passw:
        print("WELCOME TO AIRLINE RESERVATION SYSTEM!!!!!")
        t=ticket(seat1,seat2,seat3,seat4)
        t.customer()
        t.customers()
    else:
         print("Your Password Is Incorrect!")
else:
    print("Username Is Incorrect!")
	
