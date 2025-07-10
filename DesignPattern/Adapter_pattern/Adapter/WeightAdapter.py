from Adapter.Adapter import Adapter
from Adaptee.Adaptee import Adaptee

class WeightAdapter(Adapter):

    def __init__(self, weightAdaptee: Adaptee):
        self.weightAdaptee = weightAdaptee
    
    def getWeightInKg(self):
        return self.weightAdaptee.getWeight() / 2