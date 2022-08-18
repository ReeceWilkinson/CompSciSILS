def OR():
    in1 = int(input("What is the first input?"))
    in2 = int(input("What is the second input?"))
    if in1 == 1 or in2 == 1:
        return 1
    else:
        return 0

def AND():
    in1 = int(input("What is the first input?"))
    in2 = int(input("What is the second input?"))
    if in1 == 1 and in2 == 1:
        return 1
    else:
        return 0

def XOR():
    in1 = int(input("What is the first input?"))
    in2 = int(input("What is the second input?"))
    if in1 == in2:
        return 0
    else:
        return 1

def NAND():
    in1 = int(input("What is the first input?"))
    in2 = int(input("What is the second input?"))
    if in1 == 1 and in2 == 1:
        return 0
    else:
        return 1

def NOR():
    in1 = int(input("What is the first input?"))
    in2 = int(input("What is the second input?"))
    if in1 == 0 and in2 == 0:
        return 1
    else:
        return 0

def NOT():
    in1 = int(input("What is the input?"))
    if in1 == 1:
        return 0 
    else:
        return 1

def choice():
    while True:
        gateChoice = input("What Logic Gate would you like to use?").upper()
        print("Only use the inputs. 1 and 0.")
        if gateChoice == 'OR':
            print(OR())
            break
        elif gateChoice == 'AND':
            print(AND())
            break
        elif gateChoice == 'NOT':
            print(NOT())
            break
        elif gateChoice == 'NAND':
            print(NAND())
            break
        elif gateChoice == 'XOR':
            print(XOR())
            break
        elif gateChoice == 'NOR':
            print(NOR())
            break
        else:
            print("Not a valid Logic Gate. Please choose from 'OR' , 'AND' , 'NOT' , 'XOR' , 'NAND' or 'NOR'.")

choice()
