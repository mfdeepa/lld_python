from abc import ABC


from lld.design_pattern.abstractFactory.factory.AndroidCheckBoxFactory import AndroidCheckBoxFactory
from lld.design_pattern.abstractFactory.factory.FactoryAbc import Factory
from lld.design_pattern.abstractFactory.factory.androidButtonFactory import AndroidButtonFactory


class AbstractAndroidFactory(Factory):
    def create_button(self):
        return AndroidButtonFactory()

    def create_checkbox(self):
        return AndroidCheckBoxFactory()