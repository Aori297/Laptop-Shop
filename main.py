from datetime import date, time
from files.operations import *
from files.read import *
from files.write import *

lap_dict = readFile()


def main():  
    loop = True   
    while loop == True:
        print("The Notebook Warehouse".center(100))
        print("Basundhara, Kathmandu".center(100))
        print("-" * 100)
        print("1. Sell Laptops")
        print("2. Purchase Laptops")
        print("3. Exit")
        print("_" * 100)
        print()
        
        option = input("What would you like to do? ")
        
        if option == "1":
            choosenLaptop = []
            name, address, phone = userinput()
            buyMore = True
            stockLaptop(lap_dict)
            while buyMore == True:
                print("\n")
                snNum = serialNum()
                qNum = quantity(snNum)
                while qNum == -1:
                    qNum = quantity(snNum)
                qNum = int(qNum)
                updateQuantity(snNum, qNum, laptop_dict)
                lap_dict[snNum][3] = int(lap_dict[snNum][3]) - int(qNum)
                choosenLaptop = updateList(snNum, laptop_dict, qNum, choosenLaptop)

                MoreLaptop = input("Do you want to buy another laptop? (Yes/No): ")
                if MoreLaptop == "yes" or MoreLaptop == "Yes" or MoreLaptop == "Y" or MoreLaptop == "y":
                    buyMore = True
                else:    
                    sellingBill(name, address, phone, choosenLaptop)
                    buyMore = False







        elif option == '2':
            choosenLaptop = []
            distributername = manufacturerInput()    
            buy_stockLaptop(lap_dict)
            buyMore = True
            while buyMore == True:
                print("\n")
                snNum = buy_serialNum()
                qNum = buy_quantity(snNum)
                while qNum == -1:
                    qNum = buy_quantity(snNum)
                buy_updateQuantity(snNum, qNum, laptop_dict)
                lap_dict[snNum][3] = int(lap_dict[snNum][3]) + int(qNum)
                choosenLaptop = buy_updateList(snNum, laptop_dict, qNum, choosenLaptop)

                MoreLaptop = input("Do you want to restock another laptop?(Yes/No): ")
                if MoreLaptop == "yes" or MoreLaptop == "Yes" or MoreLaptop == "Y" or MoreLaptop == "y":
                    buyMore = True
                else:    
                    purchaseBill(distributername, choosenLaptop)
                    buyMore = False






        elif option == '3':
            print("\n")
            print("Exitting...")  
            loop = False
        else:
            print("Invalid input ... ")
            print()

main()
