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

        try:
            option = int(input("What would you like to do? "))
            if option >= 1 and option <= 3:
                if option == 1:
                    # Sell laptops
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
                        while MoreLaptop.lower() not in ['yes', 'no']:
                            MoreLaptop = input("Invalid input. Please enter 'Yes' or 'No': ")
                        if MoreLaptop.lower() == "yes":
                            buyMore = True
                        else:
                            sellingBill(name, address, phone, choosenLaptop)
                            buyMore = False


                elif option == 2:
                    # Purchase laptops
                    choosenLaptop = []
                    distributername = manufacturerInput()    
                    stockLaptop(lap_dict)
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

                        MoreLaptop = input("Do you want to buy another laptop? (Yes/No): ")
                        while MoreLaptop.lower() not in ['yes', 'no']:
                            MoreLaptop = input("Invalid input. Please enter 'Yes' or 'No': ")
                            buyMore = True
                        else:    
                            purchaseBill(distributername, choosenLaptop)
                            buyMore = False

                elif option == 3:
                    # Exit
                    print("\n")
                    print("Exiting...")
                    loop = False
            else:
                print("Invalid input. Please enter a valid option (1-3).")
                print()
        except ValueError:
            print("Invalid input. Please enter a valid option (1-3).")
            print()


main()
