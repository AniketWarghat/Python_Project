"""
ATM Simulator
Author: Aniket M. Warghat
Description: A simple CLI ATM Simulator Where User Can login,Check,Deposit,Withdraw The Amount from Account. 
"""

# Storing user credentials and balances in a nested dictionary
bank_account = {"Aniket":{"pin":9834,"balance":50000},
                "Aaron":{"pin":9922,"balance":50000}}

error = "Error, Enter Numeric Value!"

# Taking initial input for the account lookup
holder_name = str(input("Enter Account Holder Name : "))

authenticated = False

# Check if the name exists in our records
if holder_name in bank_account:
        try:
            # Verify the security PIN
            pin_number = int(input("Enter your PIN : "))
            if pin_number == bank_account[holder_name]["pin"]:
                print(f"Login Successful! Welcome {holder_name} \n")
                authenticated = True # Access granted
            else:
                print("Incorrect Pin.")
        except ValueError:
            # Handle non-numeric PIN entries
            print(error)
else:
        print(f"No Account Holder Found Named {holder_name} \n")
        
print("Welcome TO ATM Simulator. \n")


# This loop only runs if authenticated is set to True
while authenticated:
        
        print("1.Check Balance | 2.Deposit Money | 3.Withdraw Money |4.Logout")
        
        try:
            option = int(input("Enter your Option (1-4) : "))


            if option == 1:
                Avail_balance = bank_account[holder_name]["balance"]
                print(f"Available Balance is {Avail_balance} Rs. \n")


            elif option == 2:
                deposit_amount = float(input("Enter Amount To Deposit : "))
                bank_account[holder_name]["balance"] += deposit_amount
                print(f"Deposit Complete, Available Balance is {bank_account[holder_name]['balance']} Rs. \n")


            elif option == 3:
                withdraw_amount = float(input("Enter Amount To Withdraw : "))
                if withdraw_amount <= bank_account[holder_name]["balance"]:
                    bank_account[holder_name]["balance"] -= withdraw_amount
                    print(f"Withdrawal Complete, Available Balance is {bank_account[holder_name]['balance']} Rs. \n")
                else:
                    # Logic to prevent negative balance
                    print(f"insufficient Balance! Your Current Balance is {bank_account[holder_name]['balance']} Rs.")

            elif option == 4:
                print("Good Bye! See you next time")
                authenticated=False # Breaks the loop
            else:
                print("Enter Correct Option between 1-4")

        except ValueError:
            # Handle non-numeric inputs for options or amounts
            print(error)