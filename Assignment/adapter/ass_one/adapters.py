from abc import ABC,abstractmethod


class TravelInsuranceAdapter(ABC):
    @abstractmethod
    def add_claim(self, amount):
        pass
    @abstractmethod
    def get_status(self, claim_id):
        pass

class TravelGuardAdapter(TravelInsuranceAdapter):
    # def __init__(self, api):
    #     self.api = api

    def add_claim(self, amount):
        claim_id = "some_unique_id"  # Generate or obtain a unique claim ID
        self.api.submit_claim(claim_id, amount)
        return claim_id

    def get_status(self, claim_id):
        return self.api.get_claim_status(claim_id)


class AutoProtectAdapter(TravelInsuranceAdapter):
    # def __init__(self, api):
    #     self.api = api

    def add_claim(self, amount):
        return self.api.add_claim(amount)

    def get_status(self, claim_id):
        return self.api.get_status(claim_id)
