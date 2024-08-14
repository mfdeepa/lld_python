from lld.design_pattern.abstractFactory.ulElements.checkbox import Checkbox


class AndroidCheckbox(Checkbox):
    def click(self):
        print("Android Check Box clicked")