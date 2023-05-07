

def sellingBill(name, address, phone, choosenLaptop):
    total = 0
    shipping = 150
    for i in choosenLaptop:
      total+=int(i[3])
    grandTotal = total + shipping
    # date = datetime.now()

    print("\n")
    print("The Notebook Warehouse".center(100))
    print("Basundhara, Kathmandu".center(100))
    print("\n")
    print("---------------------------------------------------------------------------------------------------------")
    print("Name:", name)
    print("Address:", address)
    print("Phone:", phone)
    print("------------------------------------------------------------------------------------------")
    print("|S.N.     |Device Name \t\t |Company Name \t\t |Quantity\t |Price \t |")
    print("------------------------------------------------------------------------------------------")
    
    count = 1
    for i in choosenLaptop:
        print (count,"\t",i[0], "\t\t\t", i[1], "\t\t\t", i[2], "\t\t\t", i[3],  "\t\t\t","\n")
        count+=1

    print("Shipping Cost", shipping)
    print("Grand Total", grandTotal)


def purchaseBill():
    print("------------------------------------------------------------------------------------------")
    print("|S.N.     |Device Name \t\t |Company Name \t\t |Quantity\t |Price \t |")
    print("------------------------------------------------------------------------------------------")