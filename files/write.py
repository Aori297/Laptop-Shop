def sellingBill(name, address, phone, choosenLaptop):
    total = 0
    shipping = 150
    for i in choosenLaptop:
      total+=int(i[4])
    grandTotal = total + shipping
    # date = datetime.now()

    print("\n")
    print("The Notebook Warehouse".center(100))
    print("Basundhara, Kathmandu".center(100))
    print("\n")
    print("Generating Bill...")
    print("---------------------------------------------------------------------------------------------------------")
    print("Name:", name)
    print("Address:", address)
    print("Phone:", phone)
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
