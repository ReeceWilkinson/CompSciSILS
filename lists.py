numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# Appends the numbers 1-3 and the strings 'hello' and 'world' to the pre-defined arrays
second_name = names[1]
numbers.extend([1,2,3])
strings.extend(["hello","world"])

# this code just outputs the arrays and the second name on the names array (index 1)
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)