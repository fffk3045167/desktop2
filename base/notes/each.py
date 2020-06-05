
class Each():
    """包相对导入"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print(self.a)

    def add(self):
        sum = self.a + self.b
        print(sum)