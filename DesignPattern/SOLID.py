# Liskov Principle


class Vehicle:
    def numberOfWheels(self):
        return 2

class EngineVehicle(Vehicle):
    def engineType(self):
        return "combustion"

class Car(EngineVehicle):
    pass

class MotorCycle(EngineVehicle):
    pass

class Bicycle(Vehicle):
    pass

if __name__=="__main__":
    vehicleList: Vehicle = []
    vehicleList.append(Car())
    vehicleList.append(MotorCycle())
    vehicleList.append(Bicycle())
    
    for vehicle in vehicleList:
        print(vehicle.engineType())
