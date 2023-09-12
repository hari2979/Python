tamil = int(input("Tamil:"))
physics = int(input("physics:"))
maths = int(input("Maths:"))
chemistry = int(input("Chemistry:"))
computer = int(input("Computer:"))
english = int(input("English:"))
average = int(tamil+physics+maths+chemistry+computer+english)/6
if(average>35):
    print ("No additional class needed")
else:
    print ("Need an additional class to score good marks in exam")