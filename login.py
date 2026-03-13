username = "admin"
password = "12345"

user = input("Enter Username: ")
pasw = input("Enter Password: ")

if user == username and pasw == password:
    print("Login Successful")
else:
    print("Invalid Username or Password")