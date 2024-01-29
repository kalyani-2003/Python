class Demo:
    def __init__(self):
        print("In Constructor")

    def Fun(self):
        print("In Fun Method")

class Child(Demo):
    def __init__(self):
        print("In Child Constructor")

    def Gun(self):
        print("In Method Gun")

obj=Demo()
obj.Fun()
obj1=Child()
obj1.Gun()

