#REGULAR EXPRESSIONS
"""
\d matches digits (0-9)
\w
\s matches any whitespace character
.:
*:
+:
?:
[]
[^]
^:
$:

"""
#matching and searching
#regex re.match(),re.search(),re.findall()

#Example1
import re

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)



txt = "hello planet"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x = re.findall("he.+o", txt)

print(x)



#Example 2 validate emaillformat or email address
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Example usage:
email = "example@example.com"
if validate_email(email):
    print("Email is valid.")
else:
    print("Email is not valid.")


#Generators and Iterators

# Generator example
# A generator is a special type of iterator that is defined using a function and the yield keyword
def my_generator(max_num):
    current = 0
    while current < max_num:
        current += 1
        yield current

# Usage of the generator
gen = my_generator(5)
for num in gen:
    print(num)

#example
def square_generator():
    for num in range(1, 11):
        yield num ** 2

# Usage of the generator
gen = square_generator()
for square in gen:
    print(square)

#Decorators 
def my_decorator(func):
    def inner():
        print("This is the decorator")
        func()
        return inner
    
    @my_decorator
    def outer_decorator():
        print("This is outer decorator")
    outer_decorator()  