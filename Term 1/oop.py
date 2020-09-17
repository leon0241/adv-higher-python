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
        self.description = "Delivery " + str(self.deliveryNumber) + "is for " + self.deliveryType + " goods with acceptance set to " + str(self.accepted)
        return self.description

# create an instance of the super and sub-classes
FreshBakesLtd = Delivery(0, "", False, "")
#super-class with dummy properties

#now set the properties individually to show setters work
FreshBakesLtd.setDeliveryNumber(103956)
FreshBakesLtd.setDeliveryType("Fresh")
FreshBakesLtd.setAccepted(True)

#test they have worked with the getters
print("Delivery " + str(FreshBakesLtd.getDeliveryNumber()) + " is for " + FreshBakesLtd.getDeliveryType() + " goods" + " with acceptance is set to " + str(FreshBakesLtd.getAccepted()))
