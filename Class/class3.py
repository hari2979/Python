class teacher:
    def __init__(self,name,reg):
        self.name = name
        self.regno = reg
    def display(self):
        print ("Name of the staff: ", self.name)
        print ("Reg no of the staff: ", self.regno)
t1=teacher("Harikrishnan", "1")
t2=teacher("Kiran", 2)
print (t1.name)
print (t1.regno)
print (t2.name)
print (t2.regno)
t1.display()
t2.display()