#all used modules
import time
import os
import pickle

import logos
from tqdm import tqdm#following command to be executed in terminal (pip install tqdm) 



tax = 18
available_cars = {
    'WAGONR':['Price = 550000','City Mileage = 20kmpl','Engine Displacement = 1000','Power = 88.50hp'],
    'SWIFT':['Price = 800000','City Mileage = 25kmpl','Engine Displacement = 1100','Power = 90hp'],
    'ALTO':['Price = 300000','City Mileage = 20kmpl','Engine Displacement = 800','Power = 78hp'],
    'FRONX':['Price = 1300000','City Mileage = 24kmpl','Engine Displacement = 1200','Power = 100hp'],
    'CIAZ':['Price = 1400000','City Mileage = 25kmpl','Engine Displacement = 1500','Power = 105hp']
    }
detailsofcars = {
    "WAGONR": "Mileage = 24.43 kmpl \nFuel Type = Petrol \nEngine Displacement = 1000 cc \nNo. of Cylinders = 4\nMax Power = 88.50bhp@6000rpm\nMax Torque = 113Nm@4400rpm \nSeating Capacity = 5\nTransmission Type = Automatic \nBoot Space = 341 Litres\nFuel Tank Capacity = 32 Litres \nBody Type = Hatchback\n",
    
    "SWIFT": "Mileage = 25.75 kmpl\nFuel Type = Petrol\nEngine Displacement = 1100 cc\nNo. of Cylinders = 3\nMax Power = 90bhp@5700rpm \nMax Torque = 111.7Nm@4300rpm\nSeating Capacity = 5\nTransmission Type = Automatic\nBoot Space = 265 Litres\nFuel Tank Capacity = 37 Litres\nBody Type = Hatchback\nGround Clearance Unladen = 163 mm",
    
    "ALTO": "Mileage = 25.75 kmpl\nFuel Type = Petrol\nEngine Displacement = 800 cc\nNo. of Cylinders = 3\nMax Power = 78bhp@5700rpm\nMax Torque = 111.7Nm@4300rpm\nSeating Capacity = 5\nTransmission Type = Automatic\nBoot Space = 265 Litres\nFuel Tank Capacity = 37 Litres\nBody Type = Hatchback\nGround Clearance Unladen = 163 mm",
    
    "FRONX": "Mileage = 20.01 kmpl\nFuel Type = Petrol\nEngine Displacement = 1200 cc\nNo. of Cylinders = 3\nMax Power = 100bhp@5500rpm\nMax Torque = 147.6Nm@2000-4500rpm\nSeating Capacity = 5\nTransmission Type = Automatic\nBoot Space = 308 Litres\nFuel Tank Capacity = 37 Litres\nBody Type = SUV\n",
    
    "CIAZ": "Mileage = 20.04 kmpl\nFuel Type = Petrol\nEngine Displacement = 1500 cc\nNo. of Cylinders = 4\nMax Power = 105bhp@6000rpm\nMax Torque = 138Nm@4400rpm\nSeating Capacity = 5\nTransmission Type = Automatic\nBoot Space = 510 Litres\nFuel Tank Capacity = 43 Litres\nBody Type = Sedan\n"
}


#loading screen
def load():
    for i in tqdm(range(10)):
        time.sleep(0.1)
def head():
    print("-"*148)
def cls():
    os.system('cls')
#filecreation
def file_creator():
    first_time = input("Are you using this the first time?? : (Y/N)".center(148))
    if not os.path.isdir("C:\maruti") :
        os.mkdir("C:/maruti")
        file = open("C:/maruti/balance.txt","w")
        balance = "100000000"
        file.write(balance)
        file.close()    
        file = open("C:/maruti/showroom_stock.dat","wb")
        name_qtn = []
        all = []
        carname = list(available_cars)
        for i in carname:
            name_qtn.append(i)
            name_qtn.append(0)
            all.append(name_qtn)
            name_qtn = []
        pickle.dump(all,file)
        file.close()
        file = open("C:/maruti/customer_details.dat","wb")
        file.close()
#PURCHASHING BLOCK
def update_stock(choice,qtn):
    file = open("balance.txt","r")
    bal = float(file.read())
    speclist2 = available_cars.get(choice.upper())
    price2 = int(speclist2[0][8::])
    if bal < price2*qtn:
        print("Insufficient balance!!".center(148))
        return
    file.close()
    choice = choice.upper()
    file = open('showroom_stock.dat','rb')
    try:     
        prev_rec = pickle.load(file)     
    except EOFError:
        file.close
    file = open('showroom_stock.dat','wb')
    data = [choice,qtn]
    for i in range(len(prev_rec)):
        if prev_rec[i][0] == choice:
            prev_rec[i][1] += qtn   
    pickle.dump(prev_rec, file)
    file.close()
    file = open('balance.txt','r')
    available_balance = float(file.read())
    file.close()
    specs_list = available_cars.get(choice)
    price_str = specs_list[0]
    ammount = float(price_str[8::])*int(qtn)
    leftover = available_balance - ammount
    file = open('balance.txt','w')
    file.write(str(leftover))
    file.close()
def purchase():
    cls()
    load()
    cls()
    for i in available_cars:
        head()
        print(i.center(148))
        details = available_cars.get(i)
        head()
        for j in details:
            print(j.center(148))
    head()
    nfile = open("balance.txt","r")
    s = nfile.read()
    print(f"Available balance = {s}".center(148))
    print('Now make a choice among these cars'.center(148))
    print('Enter the name of the car you want to purchase    '.center(148))
    choice = input(' '.center(74)).upper()
    print('Enter the quantity of car you want to purchase    '.center(148))
    quantity = int(input(''.center(74)))
    update_stock(choice,quantity)
    print("The stock has been updated!".center(148))
#PURCHASING BLOCK END
#DISPLAY BLOCK 
def display_cars():
    cls()
    load()
    cls()
    display_para = " Welcome to our showroom! We have an exceptional range of vehicles to match your style and needs.".center(148),"\n"," Whether you're looking for performance, comfort, or cutting-edge technology, we’ve got the perfect car for you.".center(148),"\n"," Let me show you our latest models and help you find your ideal ride!".center(148)
    for a in display_para:
        print(a,end="")
        #time.sleep(.02)
    print('\n')
    a = open('showroom_stock.dat','rb') 
    try:
        cars = pickle.load(a)    
    except EOFError:
        a.close()
    for car_qtn in cars:
        if car_qtn[1]>=1:
            car = car_qtn[0]
            head()
            print(car.center(148)) 
            head() 
            details = available_cars[car] 
            for spec in details:
                print(spec.center(148))
            head()
    print("Do you want to view more details about a specific car?? : (y/n)".center(148))
    specific_car = input(" ".center(74)).lower()
    if specific_car == "y":
        while specific_car == 'y':
            print("Which car? (name) :".center(148))
            which_car = input(" ".center(74))
            print('\n')
            print("Here are the details of ".center(148))
            print(which_car.upper().center(148))
            print('\n')
            print(which_car.upper().center(148))
            print(detailsofcars.get(which_car.upper()))
            specific_car = input("Do you want to view any other car? (y/n)".center(148)).lower()
    anybuy = input("Do you want to but any one of them : (y/n) ".center(148)).lower()
    if anybuy == "y":
        print("Which car? (name) :".center(148))
        which_car = input(" ".center(74))
        carsale(name = which_car)
    else:
        input("Press enter to go back to menu".center(148))
#selling of a car 
def carsale(name):
    name = name.upper()
    cls()
    load()
    cls()
    print("Your selected car is ".center(148))
    print(name.center(148))
    print("Great Choice!, let's proceed to the billing part".center(148))
    speclist = available_cars.get(name.upper())
    price = int(speclist[0][8::])
    ammount2 = (price*(tax/100))+price
    print("We want to gather more information about you :) ".center(148))
    print("Enter you'r full name :".center(148))
    namec = input(" ".center(74))
    a = True
    while a == True:
        print("Enter you'r ADDHAR NO :".center(148))
        addhar = input(" ".center(74))
        if len(addhar) == 10:
            a = False
        else: 
            print("invalid addhar pls try again".center(148))
    b = True
    while b == True:
        print("Enter you'r phone number :".center(148))
        phoneno = input(" ".center(74))
        if len(phoneno) == 10:
            b = False
        else: 
            print("invalid phone number pls try again".center(148))
    file = open("customer_details.dat","ab")
    cdata = [namec,addhar,phoneno,name]
    pickle.dump(cdata,file)
    file.close()
    print(f"Price of the car is {price} after applying gst(18%) total payable ammount is {ammount2}".center(148))
    input("Procced to pay? ".center(148))
    time.sleep(1)
    print("Ammount recived, Thank you!".center(148))
    file = open("balance.txt","r")
    prevbal = float(file.read())
    new_bal = prevbal + ammount2
    file.close()
    file = open("balance.txt","w")
    file.write(str(new_bal))
    file.close()
    file = open('showroom_stock.dat','rb')
    try:     
        prev_rec = pickle.load(file)     
    except EOFError:
        file.close()
    file = open('showroom_stock.dat','wb')
    data = [name]
    for i in range(len(prev_rec)):
        if prev_rec[i][0] == name:
            prev_rec[i][1] -= 1  
    pickle.dump(prev_rec, file)
    file.close()
    time.sleep(1)
    print("preparing your bill invoice".center(148))
    time.sleep(3)
    cls()
    bill(namec,phoneno,addhar,name,ammount2)
#bill invoice 
def bill(cname,cphone,caddhar,name,ammount):
    head()
    print("SCHOOL".center(148))
    head()
    for i in range(16):
        print(logos.logo_lines[i].center(148))
    print("MARUTI".center(148))
    head()
    print("NAME".center(37),end="")
    print("CAR".center(37),end="")
    print("ADDHAR".center(37),end="")
    print("PHONE NUMBER".center(37))
    head()
    print(cname.center(37),end="")
    print(name.center(37),end="")
    print(caddhar.center(37),end="")
    print(cphone.center(37))
    head()
    print("Ammount paid : ",ammount)
#viewing company stock
def viewstock():
    cls()
    load()
    cls()
    file = open("showroom_stock.dat","rb")
    alldata = pickle.load(file)
    head()
    print("SCHOOL".center(148))
    head()
    print("CAR".center(74),end="")
    print("QUANTITY".center(74))
    head()
    for i in range(len(alldata)):
        print(f"{alldata[i][0]}".center(74),end="")
        print(f"{alldata[i][1]}".center(74))
    print("\n")
    file.close()
    file = open("balance.txt","r")
    print(f"The showroom have {file.read()}$ available in account".center(148))
    input("Press enter to go back".center(148))
    cls()
def user_details():
    cls()
    file = open("customer_details.dat","rb")
    head()
    print("SCHOOL".center(148))
    head()
    print("NAME".center(37),end="")
    print("ADDHAR".center(37),end="")
    print("PHONE NUMBER".center(37),end="")
    print("CAR".center(37))
    head()
    input()
    cls()
    while True:
        try:
            cvdata = pickle.load(file)
            cvname,vname,cvaddhar,cvphone = cvdata[0],cvdata[1],cvdata[2],cvdata[3]
            print(cvname,end=""*20)
            print(vname.center(20),end=""*20)
            print(cvaddhar.center(20),end=""*20)
            print(cvphone.center(20))
        except EOFError:
            break
#quit
def quit():
    cls()
    load()
    cls()
    print("Thank you for visiting our showroom please visit again!!")
    input()
    return









#_____MAIN______
cls()
file_creator()
cls()
load()
cls()
head()
print("SCHOOL".center(148))
head()
for i in logos.logo:
    print(i.center(148))
print("Welcome to Maruti Car Showroom!!".center(148))
welcome_para = " Welcome to Maruti Suzuki! I’m Sahaj, and I’m excited to help you find your ideal car.".center(148),"\n"," Our showroom offers a variety of vehicles,".center(148),"\n"," from compact cars to family SUVs,all known for reliability and fuel efficiency. Feel free to explore.".center(148),"\n"," We’re here to make your experience smooth, with flexible financing options and dedicated customer support.".center(148),"\n"," Let’s find the perfect Maruti Suzuki for you!    ".center(148),"\n","PRESS ENTER TO CONTINUE".center(148)
time.sleep(1)
for i in welcome_para:
    print(i,end="")
    time.sleep(0.01)
input(" ")
# to clear the screen
cls()
load()
cls()
# Menu 
choice = 1
while choice != 5:
    for i in logos.mainmenu:
        print(i.center(148))
    print("\n")
    print('Which service would you like to have?'.center(148))
    print('1. Purchasing a car from the Company'.center(148))
    print('2. Sell a car'.center(148))
    print('3. View company stock'.center(148))
    print("4. View customer details".center(148))
    print('5. Exit'.center(148))
    print("Enter your choice".center(148))
    choice_user = int(input(' '.center(74)))
    if choice_user == 1:
        cont = "y"
        while cont == "y":
            purchase()
            cont = input('Do you want to purchase more? (y/n) \n'.center(148))
        cls()
    elif choice_user == 2:
        display_cars()
        cls()
    elif choice_user == 3:
        viewstock()
    elif choice_user == 4:
        user_details()
    elif choice_user == 5:
        quit()
        choice = 5
        break