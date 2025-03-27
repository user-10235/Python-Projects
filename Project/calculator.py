import os

openString = "Integer Calcuator App\n1) Start\n2) Exit"

def is_convertible_to_int(s):
    try:
        a = int(s)
        return True
    except ValueError:
        return False



def equation(operator):
    firstValue = True

    while firstValue:
        first = input("Enter the first number --> ")

        if is_convertible_to_int(first):
            first = int(first)
            break
        else:
            print("Please enter an integer")

    secondValue = True

    while secondValue:
        second = input("Enter the second number --> ")

        if is_convertible_to_int(second):
            second = int(second)
            break
        else:
            print("Please enter an integer")

    if operator == "+":
        value =  first + second
        equation = str(first)+" + "+str(second)+" = "+str(value)
        history.append(equation)
        print(equation)
    elif operator == "-":
        value =  first - second
        equation = str(first)+" - "+str(second)+" = "+str(value)
        history.append(equation)
        print(equation)
    elif operator == "*":
        value =  first * second
        equation = str(first)+" * "+str(second)+" = "+str(value)
        history.append(equation)
        print(equation)
    elif operator == "/":
        value = first / second
        equation = str(first)+" / "+str(second)+" = "+str(value)
        history.append(equation)
        print(equation)
    elif operator == "%":
        value = first % second
        equation = str(first)+" % "+str(second)+" = "+str(value)
        history.append(equation)
        print(equation)




menu = True
calcMenu = True
opMenu = True
history = []


while menu:

    os.system("cls")

    print(openString)
    inStr = int(input("Enter user option --> "))

    if inStr == 1:
        calcMenu = True
    elif inStr == 2:
        os.system("cls")
        break
    else:
        calcMenu = False
        print("Invalid selection")

    while calcMenu:

        os.system("cls")

        print("Choose operation\n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n5) Modulus\n6) History\n7) Back")
        inOp = input("Enter operation choice --> ")
        if is_convertible_to_int(inOp):
            
            inOp = int(inOp)
            


        if inOp == 1 or inOp == 2 or inOp == 3 or inOp == 4 or inOp == 5 or inOp == 6 or inOp == 7:
            

            if inOp == 1:
                equation("+")
            elif inOp == 2:
                equation("-")
            elif inOp == 3:
                equation("*")
            elif inOp == 4:
                equation("/")
            elif inOp == 5:
                equation("%")
            elif inOp == 6:
                for i in range(len(history)):
                    print(str(history[i]))
            elif inOp == 7:
                calcMenu = False
        else:
            print("Invalid selection")


        back = input("Back")
