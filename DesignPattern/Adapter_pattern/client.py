# Client understands response only in Kgs not in pounds

from Adaptee.WeightAdaptee import WeightAdaptee
from Adapter.WeightAdapter import WeightAdapter

if __name__=="__main__":

    weightAdapter = WeightAdapter(WeightAdaptee(500))
    
    print(weightAdapter.getWeightInKg())