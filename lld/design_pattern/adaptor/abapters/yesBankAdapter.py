from lld.design_pattern.adaptor.abapters.BankAdapterAbc import BankAdapterAbc
from lld.design_pattern.adaptor.Banks.yesBank import YesBank


class YesBankAdapter(BankAdapterAbc):

    def __init__(self):
        self.bank = YesBank()

    def checkBalance(self):
        self.bank.balance()


