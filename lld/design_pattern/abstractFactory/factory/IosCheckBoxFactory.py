from lld.design_pattern.abstractFactory.factory.FactoryAbc import Factory
from lld.design_pattern.abstractFactory.ulElements.androidCheckBox import AndroidCheckbox
from lld.design_pattern.abstractFactory.ulElements.checkbox import Checkbox


class IosCheckBoxFactory(Factory):
    def create(self):
        return AndroidCheckbox()