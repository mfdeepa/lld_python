
class PhonePe:
    def __init__(self,Adapter):
        self.bankAdapter = Adapter

    def checkBalance(self):
        return self.bankAdapter.checkBalance()