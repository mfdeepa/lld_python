class Computer(object):
    def __init__(self):
        self.ram = None
        self.cpu = None
        self.gpu = None
        self.power_supply = 0
        self.storage = 0

    def set_ram(self, ram):
        self.ram = ram

    def set_cpu(self, cpu):
        self.cpu = cpu

    def set_gpu(self, gpu):
        self.gpu = gpu

    def set_storage(self, storage):
        self.storage = storage

    def get_ram(self):
        return self.ram

    def get_cpu(self):
        return self.cpu

    def get_gpu(self):
        return self.gpu

    def get_storage(self):
        return self.storage

    def set_power_supply(self, power_supply):
        self.power_supply = power_supply
        #return self

    def build(self):
        c = Computer()
        c.set_power_supply(self.power_supply)
        c.set_storage(self.storage)
        c.set_ram(self.ram)
        return c