class Basic:

    def __init__(self):
        self.a = 600


class Basic2:

    def __init__(self):
        self.b = 500

# Operator overloading
    def __add__(self, other):
        self.sum = self.b + other.a

        return self.sum

class Basic3():

    def __init__(self):
        self.c = 700

# Operator overloading
    def __add__(self, other):
        return self.c + other.sum


obj1 = Basic()
obj2 = Basic2()
obj3 = Basic3()

print(obj2 + obj1)
print(obj3 + obj2)

