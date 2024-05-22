class Asko:
    def __init__(self, name):
        self.n = name

    def info(self):
        return self.n

class Nursultan(Asko):
    def __init__(self):
        super().__init__("Nursulan")