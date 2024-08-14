from lld.design_pattern.observerDp.observers.observer import Observer


class Zomato(Observer):
    def update(self, temp, hum):
        if hum > 20:
            print("Zomato update price of delivery...")
        if hum <= 20:
            print("Zomato update price increased already increase of delivery..")
