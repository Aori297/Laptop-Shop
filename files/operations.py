# all the buy and sell operations here
from files.read import *
laptop_dict = readFile()



def userinput():
    
    while True:
         name = input("Enter name: ")
         if name.isalpha():
           break
         else:
           print("Invalid input. Please enter only alphabetical characters.")

    while True:
            address = input("Enter address: ")
            if address.isalpha():
              break
            else:
                 print("Invalid input. Please enter only alphabetical characters.")
    # Validating Phone Number to make sure it is a integer
    while True:
        phone = input("Enter phone number: ")
        if phone.isdigit():
            break
        else:
            print("Invalid input. Phone number must be a integer.")
    return name, address, phone


def serialNum():
    try:
            snNum = int(input("Enter the Serial number of the laptop you want to purchase"))
            if snNum <= 0 or snNum > len(laptop_dict):
                 print("Invalid Serial number. Serial number must be a integer between 0 and", len(laptop_dict))
                 snNum = serialNum()
    except:
            print("Invalid input")
    return snNum


def quantity(snNum):
    try:
            qNum = int(input("Enter the quantity"))
            if qNum <= 0 or qNum > int(laptop_dict[snNum][3]):
                 print("Invalid Quantity. Quantity must be between 0 to", int(laptop_dict[snNum][3]))
                 qNum = quantity(snNum)
    except:
            print("Invalid input")
    return qNum 

def updateList(snNum, laptop_dict, qNum, choosenLaptop):
         prodName = laptop_dict[snNum][0]
         companyName = laptop_dict[snNum][1]
         prodQuantity = qNum
         # prodPrice = laptop_dict[snNum][2]
         selectedPrice = laptop_dict[snNum][2].replace("$", " ")
         totalPrice = int(selectedPrice) * int(prodQuantity)
         companyName = laptop_dict[snNum][1]

         choosenLaptop.append([prodName, companyName, prodQuantity, selectedPrice, totalPrice])

         return choosenLaptop
     

def updateQuantity(snNum, qNum, laptop_dict):
     laptop_dict[snNum][3] = int(laptop_dict[snNum][3]) - int(qNum)
     
     file = open("laptop.txt", "w")
     for values in laptop_dict.values():
         file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
         file.write("\n")
     file.close()



# ! baki xa
def stockLaptop(lap_dict):
    print("-----------------------------------------------------------------------------------------------------------------")
    print("|S.N.   |Device Name \t\t |Manufacturer\t |Price \t |Quantity\t |CPU\t\t|GPU \t\t|")
    print("-----------------------------------------------------------------------------------------------------------------")
    count = 1 
    for count in range(1, len(lap_dict)+1):
         print("|", count,"\t|", lap_dict[count][0], "\t", lap_dict[count][1], "\t|", lap_dict[count][2], "\t |", lap_dict[count][3], "\t\t |", lap_dict[count][4], "\t|", lap_dict[count][5],"\t|")
         count = count+1
         print("-----------------------------------------------------------------------------------------------------------------")

     

def sell(lap_dict):
    name, address, phone = userinput()
    print("Welcome")

    keep_buying = True
    while keep_buying == True:
        # stockLaptop(lap_dict)
        print("Sell")
        try:
            snNum = int("Enter the Serial number of the laptop you want to purchase")
        
        except:
            print("Invalid input")
    return snNum 









# ! Code for Purchasing Laptop
def buy_userinput():
    name = input("Enter Distributer Name: ")

    return name


def buy_serialNum():
    try:
            snNum = int(input("Enter the Serial number of the laptop you want to purchase"))
            if snNum <= 0 or snNum > len(laptop_dict):
                 print("Invalid Serial number. Serial number must be a integer between 0 and", len(laptop_dict))
                 snNum = serialNum()
    except:
            print("Invalid input")
    return snNum

def buy_quantity(snNum):
    try:
            qNum = int(input("Enter the quantity"))
            if qNum <= 0 or qNum > int(laptop_dict[snNum][3]):
                 print("Invalid Quantity. Quantity must be between 0 to", int(laptop_dict[snNum][3]))
                 qNum = quantity(snNum)
    except:
            print("Invalid input")
    return qNum 

def buy_updateList(snNum, laptop_dict, qNum, choosenLaptop):
         prodName = laptop_dict[snNum][0]
         companyName = laptop_dict[snNum][1]
         prodQuantity = qNum
         # prodPrice = laptop_dict[snNum][2]
         selectedPrice = laptop_dict[snNum][2].replace("$", " ")
         totalPrice = int(selectedPrice) * int(prodQuantity)
         companyName = laptop_dict[snNum][1]

         choosenLaptop.append([prodName, companyName, prodQuantity, selectedPrice, totalPrice])

         return choosenLaptop
     

def buy_updateQuantity(snNum, qNum, laptop_dict):
     laptop_dict[snNum][3] = int(laptop_dict[snNum][3]) + int(qNum)
     
     file = open("laptop.txt", "w")
     for values in laptop_dict.values():
         file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
         file.write("\n")
     file.close()



# ! baki xa
def buy_stockLaptop(lap_dict):
    print("-----------------------------------------------------------------------------------------------------------------")
    print("|S.N.   |Device Name \t\t |Manufacturer\t |Price \t |Quantity\t |CPU\t\t |GPU \t\t|")
    print("-----------------------------------------------------------------------------------------------------------------")
    count = 1 
    for count in range(1, len(lap_dict)+1):
         print("|", count,"\t|", lap_dict[count][0], "\t", lap_dict[count][1], "\t", lap_dict[count][2], "\t", lap_dict[count][3], "\t", lap_dict[count][4], "\t", lap_dict[count][5],"\t|")
         count = count+1
         print("-----------------------------------------------------------------------------------------------------------------")

     

def buy(lap_dict):
    name, address, phone = userinput()
    print("Welcome")

    keep_buying = True
    while keep_buying == True:
        # stockLaptop(lap_dict)
        print("Sell")
        try:
            snNum = int("Enter the Serial number of the laptop you want to purchase")
        
        except:
            print("Invalid input")
    return snNum 


# OPTION 2 
def manufacturerInput():
    
    while True:
        manufacturername = input("Enter the Name of the manufacturer: ")
        if manufacturername.isalpha():
            break
        else:
            print("Invalid input. Please enter only alphabetical characters.")

    while True:
        manufactureraddress = input("Enter the address of the manufacturer: ")
        if manufactureraddress.isalpha():
            break
        else:
            print("Invalid input. Please enter only alphabetical characters.")

    return manufacturername, manufactureraddress


