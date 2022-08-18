# sets the variables and string through the use of string formatting
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

# outputs the formatted string using the data variable to input data into the formatted string
print(format_string % data)
