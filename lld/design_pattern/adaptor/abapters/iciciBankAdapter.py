from lld.design_pattern.adaptor.abapters.BankAdapterAbc import BankAdapterAbc
from lld.design_pattern.adaptor.Banks.iciciBank import IciciBank


class IciciBankAdapter(BankAdapterAbc):

    def __init__(self):
        self.bank = IciciBank()

    def checkBalance(self):
        return self.bank.bal()