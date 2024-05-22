class Asko:
    def __init__(self, name):
        self.n = name

    def info(self):
        return self.n

class Arzygul(Asko):
    def __init__(self):
        super().__init__('Arzygul')

p = Arzygul()
print(p.info())
print('test')