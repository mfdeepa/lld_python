#from lld.design_pattern.abstractFactory.factory.abstractAndroidFactory import AbstractAndroidFactory

from lld.design_pattern.abstractFactory.factory.OSFactory import OSFactory


def Deploy(val):
    # if val == "ANDROID":
    #     Abs = AbstractAndroidFactory()
    # if val == "IOS":
    #     Abs = AbstractIosFactory()

    Abs = OSFactory(val)
    factory = Abs.decide(val)
    Button = factory.create_button(val).create()
    Button.click()
    Checkbox = factory.create_checkbox(val).create()
    Checkbox.click()

if __name__ == '__main__':
    Deploy("Android")