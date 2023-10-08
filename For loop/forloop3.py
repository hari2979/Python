count = 0
counter = 0
for h in range(1,11):
    if(h%2==0):
        count = count+1
    else:
        counter = counter+1
print ("odd:", counter)
print ("even:", count)