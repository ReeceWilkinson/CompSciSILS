
def numberChoice():
    choiceNumber = int(input("Please input a whole number:"))
    return choiceNumber


def grid(operator):
    global choiceNum 
    choiceNum = numberChoice()
    firstLine = operator + " | "
    for i in range(choiceNum):
        i += 1
        firstLine = firstLine + "%s" % i
    print(firstLine)
    print("___"*choiceNum)


def plus():
    grid('+')
    operator = '+'
    for i in range(choiceNum):
        i += 1
        nextLine = "%s | " % i
        for j in range(choiceNum):
            nextLine = nextLine + str(eval("%s%s%s" % (j,operator,i)))
        print(nextLine)

def minus():
    grid('-')
    operator = '-'
    for i in range(choiceNum):
        i += 1
        nextLine = "%s | " % i
        for j in range(choiceNum):
            nextLine = nextLine + str(eval("%s%s%s" % (j,operator,i)))
        print(nextLine)

def divide():
    grid('/')
    operator = '/'
    for i in range(choiceNum):
        i += 1
        nextLine = "%s | " % i
        for j in range(choiceNum):
            nums = str(eval("%s%s%s" % (j,operator,i)))
            nextLine += round(int(nums),2)
        print(nextLine)

def multiply():
    grid('*')
    operator = '*'
    for i in range(choiceNum):
        i += 1
        nextLine = "%s | " % i
        for j in range(choiceNum):
            nextLine = nextLine + str(eval("%s%s%s" % (j,operator,i)))
        print(nextLine)

def choice():
    operator = input("Input an appropriate operator. '+' , '-' , '/'  or '*' .")
    if operator == '+':
        plus()
    elif operator == '-':
        minus()
    elif operator == '/':
        divide()
    elif operator == '*':
        multiply()
    else:
        print("Not a valid operator. Please choose from [+ - / *]")

choice()