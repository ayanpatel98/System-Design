from MargharitaPizza import MargharitaPizza
from VegdelightPizza import VegdelightPizza
from decorators.MushroomDecorator import MushroomDecorator
from decorators.ExtraCheeseDecorator import ExtraCheeseDecorator

if __name__=="__main__":
    margharitaPizza = ExtraCheeseDecorator(MushroomDecorator(MargharitaPizza()))
    vegdelightPizza = ExtraCheeseDecorator(MushroomDecorator(VegdelightPizza()))
    print("Marghirita Pizza price is: " + str(margharitaPizza.cost()))
    print("Veg Delight Pizza price is: " + str(vegdelightPizza.cost()))