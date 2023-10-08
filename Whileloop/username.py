s_username = "Hari2979"
s_password = "HariKrish29"
username = input("Enter the username: ")
password = input("Enter the password: ")
def validate():
    if(s_username==username and s_password==password):
        return "Login successful"
    else:
        return "Access denied"
h = validate()
print(h)


# program for Username and password using validate function.