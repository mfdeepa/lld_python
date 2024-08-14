from lld.design_pattern.observerDp.observers.display import Display
from lld.design_pattern.observerDp.observers.zomato import Zomato
from lld.design_pattern.observerDp.subject.weatherStation import WeatherStation
import time
if __name__ =="__main__":
    ws = WeatherStation()   # THIS IS subject

    d1 = Display()          # observer
    z = Zomato()

    d1.registerSubject(ws)
    z.registerSubject(ws)

    ws.updateWeather(10,50)
    time.sleep(2)
    ws.updateWeather(20,100)
    time.sleep(2)

    ws.updateWeather(5,60)
    time.sleep(2)

    z.unregisterSubject(ws)

    ws.updateWeather(60,10)
    time.sleep(2)

    ws.updateWeather(10,10)
    time.sleep(2)

    ws.updateWeather(10,60)