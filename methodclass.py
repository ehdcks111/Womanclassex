
class Woman:
    def __init__(self, name, weight, height, iq):
        self.name = name
        self.weight = weight
        self.height = height
        self.iq = iq

    def eat(self):
        self.weight = int(self.weight) + 2

    def study(self):
        self.iq = int(self.iq) + 5

    def sleep(self):
        self.height = float(self.height)+0.3

    def print_info(self):
        print("----------------")
        print("name:", self.name, "weight:", self.weight, "height:", self.height, "iq:", self.iq)




