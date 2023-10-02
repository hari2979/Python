class calculator:
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b
    def add(self):
        print ("Addition:",self.num1+self.num2)
    def subtra(self):
        print ("Subtraction: ",self.num1-self.num2)
    def mul(self):
        print ("Multiply:",self.num1*self.num2)
    def divd(self):
        print ("Divide:", self.num1/self.num2)
add=calculator(10, 10)
sub=calculator(20, 15)
mul=calculator(9, 9)
divd=calculator(30, 10)
add.add()
sub.subtra()
mul.mul()
divd.divd()
