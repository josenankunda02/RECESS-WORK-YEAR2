"""DAY3
Basic operators and Expressions
Arithmetic Operators
+ Addition
- subtraction
*Multiplication
/ ZeroDivision
//Divide
%Modulus

COMPARISION Operators
== Equal to
!= Not Equal
>Greater than
<Less than
>= Graeter than or equal to
<= Less or equals to

LOGICAL OPERATORS
Logical AND 'and '
Logical OR 'or'
Logical NOT 'not'

Assignmet Operators
Assign value: '='
Add value:'+'
Add and Assign value '+='
Subtract and assign '-='
Multiply and assign value: '*='
Divide and assign value: '/='
Modulus and assign value:'%='
Exponentiate and assign value: '**='

Membership Operators:
In 'In' operators: Checks iif a value exists in a sequence
Not In: 'not in' operators: checks if a value does not exit in a sequence


IDENTITY OPERATORS
Is 'is' operator: checks if two valus are the same
Is not: 'is not' operator : checks if two values are not the same 

# """


# #EXAMPLES OF ARITHMETIC OPERATORS
# # + Addition
# x= 50+ 59
# print(x)
# # - subtraction
# y= 50-30
# print(y)
# # *Multiplication
# Cows=100
# Breeds=6
# Total=(Cows*Breeds)
# print('Total')

# # / Division
# Banana=100
# Kids=6
# Answer=Banana/Kids
# print('Answer')

# # %Modulus
# x = 17
# y = 5

# result_modulus = x % y
# print(f"The result of {x} % {y} is: {result_modulus}")
# # //Divide
# result_floor_division = x // y

# # COMPARISION Operators
# # == Equal to
# a=7
# b=5
# print(a==b)

# # != Not Equal
# a=7
# b=5
# print(a!=b)
# # >Greater than
# a=15
# b=90
# if ( a > b ):
#    print (" a is greater than b")
# else:
#    print( " a is not greater than b")

    
# # <Less than
# if ( a < b ):
#   print( " a is less than b" )
# else:
#    print( " a is not less than b")

# # >= Graeter than or equal to
# a = 5
# b = 20
# if ( b >= a ):
#    print (" b is either greater than  or equal to b")
# else:
#    print (" b is neither greater than  nor equal to b")
# <= Less or equals to


# LOGICAL OPERATORS
# Logical AND 'and '
# a=True
# b=False
# print(a and b)

# # Logical OR 'or'
# print(a or b)
# # Logical NOT 'not'
# print(not a)
# print(not b)

# # Assignmet Operators
# # Assign value: '='
# b=6
# # Add and Assign value '+='
# b+=7
# print(b)

# # Subtract and assign '-='
# k=90
# k-=8
# print(k)

# # Multiply and assign value: '*='
# n=9
# n*9
# print(n)
# # Divide and assign value: '/='
# o=50
# o/=2
# print(o)
# # Modulus and assign value:'%='
# i=9
# i%=2
# print(i)
# f=2
# # f**=4
# # print(f)
# # # Exponentiate and assign value: '**='


# # Membership Operators:
# # In 'In' operators: Checks iif a value exists in a sequence
# Animals=['Cows','Goats','Pigs','Hens','Ducks']
# if 'Goats' in Animals:
#     print('Goats are there')
#     print('Hens' in Animals)
# # Not In: 'not in' operators: checks if a value does not exit in a sequence

# print('chiks' not  in Animals)

# DENTITY OPERATORS

# # Is 'is' operator: checks if two valus are the same
# p=10
# l=10
# print(p is l)
# print(p is not l)
# print(p==l)
# # Is not: 'is not' operator : checks if two values are not the same 

# #Lists
# f=[1,3,5,6,9]
# d=[1,3,5,6,9]
# print(f is not d)
# """
# Bitwise Operator
# Bitwise are used to perform operations on individual bits in of binary numbers
# Bitwise AND
# Bitwise OR
# Bitwise XOR
# Bitwise NOT
# Bitwise Lesftshift( <<<)
# Bitwise Rightshift(>>>)
#     """
# #Examples
# # Bitwise AND (&)
# a = 10   # 1010 in binary
# b = 7    # 0111 in binary

# result = a & b
# print(result)  

# # Bitwise AND (&)
# a = 10   # 1010 in binary
# b = 7    # 0111 in binary

# result = a & b
# print(result)  # Output: 2 (0010 in binary)

# # Bitwise XOR (^)
# a = 10   # 1010 in binary
# b = 7    # 0111 in binary

# result = a ^ b
# print(result)  # Output: 13 (1101 in binary)



# #Assignment
# #Create a simple calculator Function to calculate(add,sub,mul,div)
# def add(a,b):
#     return a + b
# def sub(a,b):
#     return a - b
# def mul(a,b):
#     return a * b
# def div(a,b):
#     return a / b
# def main():
#     print('JOJOZ CALC')
#     a=float(input('Enter  a first number'))
#     b=float(input('Enter a second number'))
#     operator = input('Enter the opertor(+, -, *, /)')
    
#     if operator =='+':
#         result=add(a,b)
#     elif operator =='-':
#         result=sub(a,b)
#     elif operator =='/':
#         result=div(a,b)
#     elif operator =='*':
#         result=mul(a,b)
#     else:
#         print('Invalid operator')    
#         return
#     print('The result is' , result)   
             
# if __name__ == '__main__':
#         main()
    
        
        #tkinter learn
        #ASSIGNMENT1
        #Create a simple calculator program with a GUI interface. Make the title of the claculator program with program window with your name eg JOJO SIMPLE CALC
        
import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

window = tk.Tk()
window.title("JOJO SIMPLE CALC")

window.option_add("*Font", "Arial 20")
window.option_add("*justify", "center")

window.configure(background="black")

entry = tk.Entry(window, width=20, font=('Arial', 100))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_1 = tk.Button(window, text="1", padx=5, pady=5, bg="blue", fg="white", font=("Arial", 20),command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=20, pady=10, bg="blue", fg="white", font=("Arial", 20),command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=20, pady=10, bg="blue", fg="white",  font=("Arial", 20),command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=20, pady=10, bg="blue", fg="white",font=("Arial", 20), command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=20, pady=10, bg="blue", fg="white", font=("Arial", 20),command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=20, pady=10, bg="blue", fg="white",font=("Arial", 20), command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=20, pady=10, bg="blue", fg="white", font=("Arial", 20),command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=20, pady=10, bg="blue", fg="white", font=("Arial", 20),command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=20, pady=10, bg="blue", fg="white", font=("Arial",20),command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=20, pady=10, bg="blue", fg="white", font=("Arial", 20),command=lambda: button_click(0))
button_plus = tk.Button(window, text="+", padx=20, pady=10, bg="blue", fg="white",font=("Arial", 20), command=lambda: button_click("+"))
button_minus = tk.Button(window, text="-", padx=20, pady=10, bg="blue", fg="white",font=("Arial", 20), command=lambda: button_click("-"))
button_multiply = tk.Button(window, text="*", padx=20, pady=10, bg="blue", fg="white",font=("Arial", 20), command=lambda: button_click("*"))
button_divide = tk.Button(window, text="/", padx=20, pady=10, bg="blue", fg="white",font=("Arial", 20), command=lambda: button_click("/"))
button_equal = tk.Button(window, text="=", padx=20, pady=10, bg="blue", fg="white",font=("Arial", 20), command=button_equal)
button_clear = tk.Button(window, text="C", padx=20, pady=10, bg="blue", fg="white", font=("Arial", 20),command=button_clear)

button_1.grid(row=1, column=0, padx=50, pady=50, sticky="nsew")
button_2.grid(row=1, column=1, padx=50, pady=50, sticky="nsew")
button_3.grid(row=1, column=2, padx=50, pady=50, sticky="nsew")
button_plus.grid(row=1, column=3, padx=50, pady=50, sticky="nsew")

button_4.grid(row=2, column=0, padx=50, pady=50, sticky="nsew")
button_5.grid(row=2, column=1, padx=50, pady=50, sticky="nsew")
button_6.grid(row=2, column=2, padx=50, pady=50, sticky="nsew")
button_minus.grid(row=2, column=3, padx=50, pady=50, sticky="nsew")

button_7.grid(row=3, column=0, padx=50, pady=50, sticky="nsew")
button_8.grid(row=3, column=1, padx=50, pady=50, sticky="nsew")
button_9.grid(row=3, column=2, padx=50, pady=50, sticky="nsew")
button_multiply.grid(row=3, column=3, padx=50, pady=50, sticky="nsew")

button_0.grid(row=4, column=0, padx=50, pady=50, sticky="nsew")
button_clear.grid(row=4, column=1, padx=50, pady=50, sticky="nsew")
button_divide.grid(row=4, column=2,padx=50, pady=50, sticky="nsew")
button_equal.grid(row=4, column=3, padx=50, pady=50, sticky="nsew")

# Center the calculator in the window
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(5):
    window.grid_rowconfigure(i, weight=1)

window.mainloop()





