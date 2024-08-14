from lld.design_pattern.observerDp.observers.observer import Observer


class Display(Observer):
    def update(self,temp,humidity):
        print(f"Temp: {temp}, Humidity: {humidity} from display")