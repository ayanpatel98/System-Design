from Adaptee.Adaptee import Adaptee

class WeightAdaptee(Adaptee):
    
    def __init__(self, weight: int):
        self.weight = weight

    def getWeight(self):
        return self.weight
    