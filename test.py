import sys

while True:
  try:
    n = int(input("Amount of iterations? "))
  except Exception:
    print("Please enter a number, not a character or character*")
    exit()
  
  index = 0
  space = " "
  
  for i in range(n):
    sys.stdout.write(str(i) + " | ")
    for i in range(n+1):
      sys.stdout.write(str(i+index))
      if n >= 10:
        if i+index <= 10: 
          sys.stdout.write(" ") # increase space by one to format the grid nicely
        elif i+index >= 10:
          sys.stdout.write("") # if n <= 10 then append NO spaces
      sys.stdout.write(" ")
    #sys.stdout.write(" index: " + str(index))
    sys.stdout.write("\n")
    index += 1