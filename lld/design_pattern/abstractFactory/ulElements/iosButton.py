from lld.design_pattern.abstractFactory.ulElements.button import Button


class IosButton(Button):
    def click(self):
        print("Ios button clicked")