class a():
    def __init__(self):
        print ("Hari")
class b():
    def __init__(self):
        super().__init__()
        print ("Krishnan")
    def display(self):
        print ("b")
class c(b,a):
    def __init__(self):
        super().__init__()
        print ("Hari Krishnan")
    def display(self):
        print ("c")
name = c()




# Best example for super keyword.