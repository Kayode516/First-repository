username = "Kayode516"
password = "Iamkayode516@"

attempt = 0

while attempt < 3:

    enter_username = input("Enter Username: ")
    enter_password = input("Enter password: ")

    if enter_username == username and enter_password == password:
        print("Access Granted")
        break
    else:
        print("Access Denied")
        attempt += 1
if attempt == 3:
    print("Too many attempts, Access denied")

