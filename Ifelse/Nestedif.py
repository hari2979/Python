salary = int(input("My Salary is:"))
age = int(input("My age is:"))
if(salary>20000 or age<25):
    print ("You are eligble for loan")
    loan = int(input("Enter the loan amount:"))
    if(loan>50000):
        print ("Maxmium loan amount has been reached")
    else:
        print ("You are eliglible for loan")
else:
    print ("You are not eligible")