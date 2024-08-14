from lld.design_pattern.abstractFactory.ulElements.button import Button


class AndroidButton(Button):
    def click(self):
        print("Android button clicked")