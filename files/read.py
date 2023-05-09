# to read the laptop.txt file 
def readFile():
    file = open("laptop.txt","r")
    lap_dict = {}
    lap_id = 1 
    for line in file:
        
        # replace \n with ""
        line = line.replace("\n","")

        # updating it into the dictionary
        lap_dict.update({lap_id: line.split(",")})
        lap_id = lap_id + 1

        # returns the values of laptop dictionary
    return lap_dict