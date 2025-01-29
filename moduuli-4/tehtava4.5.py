username = "python"
password = "rules"

username_str = (input("Enter username: "))
password_str = (input("Enter password: "))

while username_str != username or password_str != password:
    print("Access denied.")
    username_str = input("Enter username: ")
    password_str = input("Enter password: ")
if username_str == username and password_str == password:
    print("Welcome!")