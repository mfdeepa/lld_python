from lld.design_pattern.abstractFactory.factory.FactoryAbc import Factory
from lld.design_pattern.abstractFactory.factory.IosButtonFactory import IosButtonFactory
from lld.design_pattern.abstractFactory.factory.IosCheckBoxFactory import IosCheckBoxFactory


# class AbstractIosFactory(Factory):
#
#     def create_button(self):
#         return IosButtonFactory()
#
#     def create_checkbox(self):
#         return IosCheckBoxFactory()

class AbstractIosFactory(Factory):
    def create_button(self):
        return IosButtonFactory()

    def create_checkbox(self):
        return IosCheckBoxFactory()