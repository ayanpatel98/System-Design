from strategy.VehicleStrategy import VehicleStrategy

class Vehicle:
    def __init__(self, vehicleStrategyObj: VehicleStrategy):
        self.vehicleStrategyObj = vehicleStrategyObj
    
    def drive(self):
        self.vehicleStrategyObj.drive()