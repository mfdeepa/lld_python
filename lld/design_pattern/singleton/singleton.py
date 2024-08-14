import threading


class Singleton:
    __instance = None
    __lock = threading.Lock()

# arrow on 6th line shows that __new__ method is call the class.
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super(Singleton, cls).__new__(cls)
                return cls.__instance

if __name__ == "__main__":
    instance1 = Singleton()
    print(instance1)
    instance2 = Singleton()
    print(instance2)
    print(instance1 is instance2)  # o/p is true as address of both instance is same.

