score = int(input("Score:"))
if(score<40):
    print ("Student has failed")
elif(score>40 and score<70):
    print ("Student has passed with average marks")
elif(score>80 and score<100):
    print ("student has passed with good marks")
else:
    print ("Invalid input")
