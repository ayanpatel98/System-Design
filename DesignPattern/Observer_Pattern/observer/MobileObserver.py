from observer.Observer import Observer
from observable.Observable import Observable

class MobileObserver(Observer):

    def update(self, observableObj: Observable):
        print("Mobile Temperature: ", observableObj.getTemp())