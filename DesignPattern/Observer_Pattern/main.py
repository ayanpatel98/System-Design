from observable.WeatherObservable import WeatherObservable
from observer.MobileObserver import MobileObserver
from observer.EmailObserver import EmailObserver

if __name__=="__main__":
    weatherObservable = WeatherObservable()
    weatherObservable2 = WeatherObservable()

    mobileObserver1 = MobileObserver()
    mobileObserver2 = MobileObserver()
    emailObserver1 = EmailObserver()

    weatherObservable.add(mobileObserver1)
    weatherObservable.add(mobileObserver2)
    weatherObservable.add(emailObserver1)

    weatherObservable2.add(mobileObserver1)
    weatherObservable2.add(mobileObserver2)
    weatherObservable2.add(emailObserver1)

    weatherObservable.setTemp(10)
    weatherObservable2.setTemp(20)
    weatherObservable.setTemp(10)
    weatherObservable2.setTemp(20)
    