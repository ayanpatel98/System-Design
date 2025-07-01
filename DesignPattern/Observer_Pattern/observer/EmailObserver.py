from observer.Observer import Observer
from observable.Observable import Observable

class EmailObserver(Observer):

    def update(self, observableObj: Observable):
        print("Email Temperature: ", observableObj.getTemp())