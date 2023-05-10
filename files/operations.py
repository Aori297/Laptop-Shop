# all the buy and sell operations here
from files.read import *
laptop_dict = readFile()


# ! displays the laptop details in a table
def stockLaptop(lap_dict):
    print("-----------------------------------------------------------------------------------------------------------------")
    print("|S.N.   |Device Name \t\t |Manufacturer\t |Price \t |Quantity\t |CPU\t\t|GPU \t\t|")
    print("-----------------------------------------------------------------------------------------------------------------")
    count = 1 
    for count in range(1, len(lap_dict)+1):
         print("|", count,"\t|", lap_dict[count][0], "\t |", lap_dict[count][1], "\t |", lap_dict[count][2], "\t |", lap_dict[count][3], "\t\t |", lap_dict[count][4], "\t|", lap_dict[count][5],"\t|")
         count = count+1
         print("-----------------------------------------------------------------------------------------------------------------")


# ! Selling Laptop Code
# ! Asks and validates user for their information
def userinput():
    # Validating name is a alphabet
    while True:
         name = input("Enter name: ")
         if name.isalpha():
           break
         else:
           print("Invalid input. Please enter only alphabetical characters.")

    # Validating address is a alphabet
    while True:
        address = input("Enter address: ")
        if address.isalpha():
            break
        else:
            print("Invalid input. Please enter only alphabetical characters.")
    # Validating Phone Number is a integer
    while True:
        phone = input("Enter phone number: ")
        if phone.isdigit():
            break
        else:
            print("Invalid input. Phone number must be a integer.")

    return name, address, phone


# ! Asks and validates the serial number of the laptop while user buys a laptop
def serialNum():
    while True:
        try:
            snNum = int(input("Enter the Serial number of the laptop you want to purchase: "))
            if snNum <= 0 or snNum > len(laptop_dict):
                print("Invalid Serial number. Serial number must be a integer between 0 and", len(laptop_dict))
            else:
                return snNum
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            


# ! Asks and validates the quantity of the laptop from laptop.txt file while buying a laptop
def quantity(snNum):
    try:
            qNum = int(input("Enter the quantity: "))
            if qNum <= 0 or qNum > int(laptop_dict[snNum][3]):
                 print("Invalid Quantity. Quantity must be between 0 to", int(laptop_dict[snNum][3]))
                 qNum = quantity(snNum)
            return qNum 
    except:
            print("Invalid input")
    return -1 


# ! Updates a list of selected laptops with the details and prices of a newly selected laptop
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


# ! Subtracts the laptops quantity when the laptop is sold
def updateQuantity(snNum, qNum, laptop_dict):
     laptop_dict[snNum][3] = int(laptop_dict[snNum][3]) - int(qNum)
     
     file = open("laptop.txt", "w")
     for values in laptop_dict.values():
         file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
         file.write("\n")
     file.close()






# ! Buying Laptop Code
# ! Asks and Validates the Distributers name
def manufacturerInput():
    while True:
        distributername = input("Enter the Name of the distributer: ")
        if distributername.isalpha():
            break
        else:
            print("Invalid input. Please enter only alphabetical characters.")
    return distributername


# ! Asks and Validates the serial name of the laptop in laptop.txt
def buy_serialNum():
    while True:
        try:
            snNum = int(input("Enter the Serial number of the laptop you want to restock: "))
            if snNum < 1 or snNum > len(laptop_dict):
                print("Invalid Serial number. Serial number must be an integer between 1 and", len(laptop_dict))
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return snNum


# ! Asks and validates the quantity from laptop.txt
def buy_quantity(snNum):
    try:
            qNum = int(input("Enter the quantity you want to restock: "))
            if qNum <= 0:
                 print("Invalid Quantity. Quantity must be between 0 to", int(laptop_dict[snNum][3]))
                 qNum = buy_quantity(snNum)
            return qNum 
    except:
            print("Invalid input")
    return -1 


# ! Updates a list of selected laptops with the details and prices of a newly selected laptop
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
     

# ! Adds the laptops quantity when the laptop is restocked
def buy_updateQuantity(snNum, qNum, laptop_dict):
     laptop_dict[snNum][3] = int(laptop_dict[snNum][3]) + int(qNum)
     
     file = open("laptop.txt", "w")
     for values in laptop_dict.values():
         file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
         file.write("\n")
     file.close()