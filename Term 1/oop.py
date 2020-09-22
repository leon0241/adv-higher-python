#Demo of uses of classes in Python
class Delivery():
    def __init__(self, deliveryNumber, deliveryType, accepted, description):
        self.deliveryNumber = deliveryNumber
        self.deliveryType = deliveryType
        self.accepted = accepted
        self.description = ""

    #Setter Methods
    def setDeliveryNumber(self, deliveryNumber):
        self.deliveryNumber = deliveryNumber
    def setDeliveryType(self, deliveryType):
        self.deliveryType = deliveryType
    def setAccepted(self, accepted):
        self.accepted = accepted

    #Getter Methods
    def getDeliveryNumber(self):
        return self.deliveryNumber
    def getDeliveryType(self):
        return self.deliveryType
    def getAccepted(self):
        return self.accepted
    def getDescription(self):
        a = str(self.deliveryNumber)
        b = self.deliveryType
        c = str(self.accepted)
        self.description = "Delivery " + a + " is for " + b + " goods with acceptance set to " + c
        return self.description

class Cold(Delivery):

    #Constructor Method
    def __init__(self, deliveryNumber, deliveryType, accepted, maxTemp, minTemp, description):
        Delivery.__init__(self, deliveryNumber, deliveryType, accepted, description)
        self.maxTemp = maxTemp
        self.minTemp = minTemp

    #setter methods
    def setMaxTemp(self, maxTemp):
        self.maxTemp = maxTemp
    def setMinTemp(self, minTemp):
        self.minTemp = minTeam

    #getter methods
    def getMaxTemp(maxTemp):
        return self.maxTemp
    def getMinTemp(minTemp):
        return self.minTemp

    #overridden method
    def getDescription(self):
        a = str(self.deliveryNumber)
        b = str(self.minTemp)
        c = str(self.maxTemp)
        d = str(self.accepted)
        self.description = "Delivery " + a + " goods between temperatures of " + b + " and " + c + " with acceptance set to " + d
        return self.description

    #end of Cold sub-class definition
class Normal(Delivery):
    #Constructor Method
    def __init__(self, deliveryNumber, deliveryType, accepted, description):
        Delivery.__init__(self, deliveryNumber, deliveryType, accepted, description)

    #getter overriden method
    def getDescription(self):
        if self.accepted:
            self.description = "Delivery " + str(self.deliveryNumber) + " is for " + self.deliveryType + " goods that have been accepted."
        else:
            self.description = "Delivery " + str(self.deliveryNumber + " is for " + self.deliveryType + " goods that have NOT been accepted.")
        return self.description
    #End of normal sub-class definition

# create an instance of the super and sub-classes
FreshBakesLtd = Delivery(0, "", False, "")
#super-class with dummy properties

#now set the properties individually to show setters work
FreshBakesLtd.setDeliveryNumber(103956)
FreshBakesLtd.setDeliveryType("Fresh")
FreshBakesLtd.setAccepted(True)

#Create instances of sub-classes
FrozenFreshFishLtd = Cold(154678, "Frozen", True, -18, -15, "")
BananasLtd = Cold(136782, "Chilled", True, 1, 4, "")
NewClothesLtd = Normal(142537, "Dry", "No", "")
FreshBodiesLtd = Cold(177013, "Frozen", True, 1, 4, "")

todaysDeliveries = [FreshBakesLtd, FrozenFreshFishLtd, BananasLtd, NewClothesLtd, FreshBodiesLtd]

#Print
print()
print("Now iterate through array to demonstrate polymorphism")
for item in todaysDeliveries:
    print(item.getDescription())
