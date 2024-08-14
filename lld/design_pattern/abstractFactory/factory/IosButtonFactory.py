from lld.design_pattern.abstractFactory.factory.FactoryAbc import Factory
from lld.design_pattern.abstractFactory.ulElements.iosButton import IosButton


class IosButtonFactory(Factory):
    def create(self):
        return IosButton()