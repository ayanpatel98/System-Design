from observable.Observable import Observable
from observer.Observer import Observer

class WeatherObservable(Observable):

    def __init__(self):
        self.observerList = []
        self.temp = 0

    def add(self, observerObj: Observer):
        self.observerList.append(observerObj)

    def remove(self, observerObj: Observer):
        self.observerList.remove(observerObj)
    
    def update(self):
        for observer in self.observerList:
            observer.update(self)
    
    def setTemp(self, t):
        self.temp+=t
        self.update()
    
    def getTemp(self):
        return self.temp