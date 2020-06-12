valid = False
password = "bruh"
while valid == False:
    attempt = input("enter a password: ")
    if attempt == password:
        valid = True
print("your password was successful")
