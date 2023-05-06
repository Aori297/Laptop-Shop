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

            # sell()
            # ! ahile ko lagi
            print("Name:", name)
            print("Address:", address)
            print("Phone:", phone)
            # ! operations ma validate

            buyMore = True
            while buyMore == True:
                stockLaptop(lap_dict)
                print("\n")

                snNum = serialNum()
                
                print("Serial Num", snNum)

                qNum = quantity(snNum)
                qNum = int(qNum)
                print("Quantity", qNum)

                updateQuantity(snNum, qNum, laptop_dict)

                choosenLaptop = updateList(snNum, laptop_dict, qNum, choosenLaptop)
                print("Laptop Sold", choosenLaptop)

                MoreLaptop = input("Do you want to buy another laptop?")
                if MoreLaptop == "yes" or MoreLaptop == "Yes":
                    buyMore = True
                else:    
                    sellingBill(name, address, phone, choosenLaptop)
                    buyMore = False

        elif option == '2':
            choosenLaptop = []
            name, address, phone = buy_userinput()

            # sell()
            # ! ahile ko lagi
            print("Name:", name)
            print("Address:", address)
            print("Phone:", phone)
            # ! operations ma validate

            buyMore = True
            while buyMore == True:
                buy_stockLaptop(lap_dict)
                print("\n")

                snNum = buy_serialNum()
                
                print("Serial Num", snNum)

                qNum = buy_quantity(snNum)
                qNum = int(qNum)
                print("Quantity", qNum)

                buy_updateQuantity(snNum, qNum, laptop_dict)

                choosenLaptop = buy_updateList(snNum, laptop_dict, qNum, choosenLaptop)
                print("Laptop Sold", choosenLaptop)

                MoreLaptop = input("Do you want to buy another laptop?")
                if MoreLaptop == "yes" or MoreLaptop == "Yes":
                    buyMore = True
                else:    
                    #sellingBill(name, address, phone, choosenLaptop)
                    buyMore = False

        elif option == '3':
            print("\n")
            print("Exitting...")  
            loop = False
        else:
            print("Invalid input ... ")
            print()

main()