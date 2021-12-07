passWord = int(input("Insert Password : \n "))
if passWord == 123:
    print("Welcome admin")
elif type(passWord) == str:
    print("password can not be string")
else:
    print("Wrong password")

    