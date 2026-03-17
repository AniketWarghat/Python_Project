def add (x,y):
    return x+y

def subtract (x,y):
    return x-y

def multiply (x,y):
    return x*y

def divide (x,y):
        if y==0:
            return ("Error 0 is not divisible, please enter valid number")
        else:
            return x/y


history = []

while True:

    print("-------------Simple Calculator-------------")
    print("1.Add | 2.Subtract | 3.Multiply | 4.Divide | 5.History | 6.Exit")

    op = (input("Enter Option 1-6 : "))

    try:
        op = int(op)

        if op < 5:

            num1 = float(input("Enter Num1 : "))
            num2 = float(input("Enter Num2 : "))

            if op == 1:
                result = add(num1,num2)
                output = f"{num1} + {num2} = {result}"
                print(output)
                history.append(output)

            elif op == 2:
                result = subtract(num1,num2)
                output = f"{num1} - {num2} = {result}"
                print(output)
                history.append(output)

            elif op == 3:
                result = multiply(num1,num2)
                output = f"{num1} * {num2} = {result}"
                print(output)
                history.append(output)

            elif op == 4:
                if num2!=0:   
                    result = divide(num1,num2)
                    output = f"{num1} / {num2} = {result}"
                    print(output)
                    history.append(output)
                else:
                    print(divide(num1,num2))

        elif op == 5:
            counter = 0
            
            if not history:
                print("No calculations yet!")
            else:
                print("------Calculation History------")
                for i in history:
                    counter+=1
                    print(f"{counter}. {i}")

        elif op == 6:
            print("Exiting Program......")
            break 

        else:
            print(f"{op} is not the valid option.")

    except:
        print(f"Error, due to '{op}' try again.")

