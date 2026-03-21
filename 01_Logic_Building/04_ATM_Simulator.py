bank_account = {"Aniket":{"pin":9834,"balance":50000},
                "Aaron":{"pin":9922,"balance":50000}}

holder_name = str(input("Enter Account Holder Name : "))

authenticated = False

if holder_name in bank_account:
    pin_number = int(input("Enter your PIN : "))
    if pin_number == bank_account[holder_name]["pin"]:
        print(f"Login Successful! Welcome {holder_name}")
        authenticated = True
    else:
        print("Incorrect Pin.")
else:
    print(f"No Account Holder Found Named {holder_name}")