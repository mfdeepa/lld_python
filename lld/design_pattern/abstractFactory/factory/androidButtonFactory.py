from lld.design_pattern.abstractFactory.factory.FactoryAbc import Factory
from lld.design_pattern.abstractFactory.ulElements.androidButton import AndroidButton


class AndroidButtonFactory(Factory):
    def create(self):
        return AndroidButton()