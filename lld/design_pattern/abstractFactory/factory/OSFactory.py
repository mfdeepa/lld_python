from lld.design_pattern.abstractFactory.factory.abstractAndroidFactory import AbstractAndroidFactory
from lld.design_pattern.abstractFactory.factory.abstractIosFactory import AbstractIosFactory


class OSFactory:
    def __init__(self, val):
        self.val = val

    def decide(self,val):
        if val == "Android":
            return AbstractAndroidFactory
        if val == "Ios":
            return AbstractIosFactory