import datetime
date = datetime.datetime.now()

def sellingBill(name, address, phone, choosenLaptop):
    total = 0
    shipping = 150
    for i in choosenLaptop:
      total+=int(i[4])
    grandTotal = total + shipping

    print("\n")
    print("The Notebook Warehouse".center(100))
    print("Basundhara, Kathmandu".center(100))
    print("\n")
    print("Generating Bill...")
    print("---------------------------------------------------------------------------------------------------------")
    print("Name:", name)
    print("Address:", address)
    print("Phone:", phone)
    print("Date:", date.strftime("%x"))
    print("---------------------------------------------------------------------------------------------------------")
    print("|S.N.     |Device Name \t\t |Company Name \t\t |Quantity\t |Price \t |Total Price\t")
    print("---------------------------------------------------------------------------------------------------------")
    
    count = 1
    for i in choosenLaptop:
        print ("|", count,"\t  |",i[0], "\t |", i[1], "\t         |", i[2], "\t         |", i[3],  "\t |",i[4])
        print("---------------------------------------------------------------------------------------------------------")
        count+=1

    print("Shipping Cost: ", shipping)
    print("Grand Total: ", grandTotal)
    print("\n")
    print("\n")
    createSellingBill(name, address, phone, choosenLaptop, shipping, grandTotal)

def purchaseBill(distributername, choosenLaptop):
    total = 0
    for i in choosenLaptop:
        total += int(i[4])
    totalsum = total
    vat = totalsum * (13/100)
    grandTotal = totalsum + vat

    print("\n")
    print("Generating Bill...")
    print("--------------------------------------------------------------------------------------------------------")
    print(" Distributer Name:", distributername,)
    print("Date:", date.strftime("%x"))
    print("--------------------------------------------------------------------------------------------------------")
    print("|S.N.     |Device Name \t\t |Manufacturer\t\t |Quantity \t |Price\t\t | Total Price  ")
    print("--------------------------------------------------------------------------------------------------------")
    count = 1
    for i in choosenLaptop:
        print (" ", count,"\t   ",i[0], "\t  ", i[1], "\t         ", i[2], "\t         ", i[3],  "\t ", i[4])
        print("--------------------------------------------------------------------------------------------------------")
        count+=1
    print("Total: ", totalsum)
    print("Vat Total: ", vat)
    print("Grand Total: ", grandTotal)
    print("\n")
    print("\n")


def createSellingBill(name, address, phone, choosenLaptop, shipping, grandTotal):
    date = datetime.datetime.now()

    date = str(date).replace(":","")

    filename = "bills/" + name + date + ".txt"
    file = open(filename, "w")
    file.write("\n")
    file.write("The Notebook Warehouse".center(100) + "\n")
    file.write("Basundhara, Kathmandu".center(100) + "\n")
    file.write("\n")
    file.write("Generating Bill...\n")
    file.write("---------------------------------------------------------------------------------------------------------\n")
    file.write("Name: "+ name)
    file.write("\nAddress: "+ address)
    file.write("\nPhone: "+ str(phone))
    date = datetime.datetime.now()
    file.write("\nDate: "+ str(date.strftime("%x")))
    file.write("\n---------------------------------------------------------------------------------------------------------\n")
    file.write("|S.N.     |Device Name \t\t |Company Name \t\t |Quantity\t |Price \t |Total Price\t\n")
    file.write("---------------------------------------------------------------------------------------------------------\n")

    count = 1
    for i in choosenLaptop:
        file.write("|"+ str(count) +"\t  |"+i[0]+ "\t |"+ str(i[1])+ "\t         |"+ str(i[2])+ "\t         |"+ str(i[3])+ "\t |"+str(i[4])+"\n")
        file.write("---------------------------------------------------------------------------------------------------------\n")
        count += 1

    file.write("Shipping Cost: "+ str(shipping))
    file.write("\nGrand Total: "+ str(grandTotal))
    file.write("\n")
    file.write("\n")

    # Close the file
    file.close()
