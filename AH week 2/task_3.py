#A car sales showroom holds data about cars in stock as shown below:

#1.  Create a modular program in Python that will:

#a.  prompt the user to enter the the car details
#b.  store the details entered in a Python record
#c.  print the details of the car from the Python record

def def_car():
    class car():
        def __init__(self):
            self.make = str
            self.model = str
            self.reg = str
            self.color = str
            self.mileage = int
            self.saleDate = str
            self.salePrice = int
    carList = [car() for i in range(10)]
    return carList

def get_details(list):
    list[0].make = input("enter a make: ")
    list[0].model = input("enter a model: ")
    list[0].reg = input("enter a registration plate: ")
    list[0].color = input("enter a colour: ")
    list[0].mileage = int(input("enter a mileage: "))
    list[0].saleDate = input("enter a sale date: ")
    list[0].salePrice = int(input("enter a sale price: "))
    return list

def print_details(list):
    print(list[0].make)
    print(list[0].model)
    print(list[0].reg)
    print(list[0].color)
    print(list[0].mileage)
    print(list[0].saleDate)
    print(list[0].salePrice)
    return list

list = def_car()
list = get_details(list)
print_details(list)
