#Exception Handling
#Exception handling is a mechanism in Python that allows you to handle and manage errors or exceptional events that occur during the execution of a program. 
# It helps in preventing your program from crashing and provides a way to gracefully handle errors.
# ZeroDivisionError: Raised when attempting to divide by zero.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    
# FileNotFoundError: Raised when a file or directory is requested but cannot be found.
try:
    file = open("example.txt", "r")
    content = file.read()
    file.close()
except FileNotFoundError:
    print("Error: The file does not exist.")
 
 # ValueError: Raised when a built-in operation or function receives an argument of the right type but an inappropriate value.
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")

#TypeError: Raised when an operation or function is applied to an object of inappropriate type.
try:
    result = "10" + 5
except TypeError:
    print("Error: Incompatible types for addition.")

#IndexError: Raised when an index is out of range
try:
    numbers = [1, 2, 3]
    value = numbers[5]
except IndexError:
    print("Error: Index out of range.")

#KeyError: Raised when a dictionary key is not found.
try:
    my_dict = {"a": 1, "b": 2}
    value = my_dict["c"]
except KeyError:
    print("Error: Key not found in dictionary.")

#IOError: Raised when an input/output operation fails.
try:
    file = open("example.txt", "r")
    content = file.read()
    file.close()
except IOError:
    print("Error: An error occurred while reading the file.")


#FILE HANDLING
#File handling in Python involves working with files, such as reading from and writing to them.
# Open a file in read mode
file = open("example.txt", "r")

# Open a file in write mode (creates a new file if it doesn't exist)
file = open("example.txt", "w")

# Open a file in append mode (appends to an existing file or creates a new file)
file = open("example.txt", "a")


#Reading from a file
# Read the entire file content
content = file.read()

# Read a single line
line = file.readline()

# Read all lines into a list
lines = file.readlines()

 #writing to a file
 # Write a string to the file
file.write("Hello, world!")

# Write multiple lines
file.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])

#closing a file
file.close()



