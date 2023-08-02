#DAY 4 OOP PYTHON
#Key Concepts
"""
   Key Concepts
    A class
   
"""
#A CLASS
# # #This is a blue print for creating objects
# # #Example:Car:
# # class Car:
# #     def __init__(self, make, model, year):
# #         self.make = make
# #         self.model = model
# #         self.year = year
# #         self.engine_status = False

# #     def start_engine(self):
# #         if self.engine_status:
# #             print("Engine is already running.")
# #         else:
# #             self.engine_status = True
# #             print("Engine started.")

# #     def stop_engine(self):
# #         if not self.engine_status:
# #             print("Engine is already stopped.")
# #         else:
# #             self.engine_status = False
# #             print("Engine stopped.")

# # # Creating an instance of the Car class
# # my_car = Car("Toyota", "Corolla", 2022)

# # # Calling methods on the my_car object
# # my_car.start_engine()  # Output: Engine started.
# # my_car.stop_engine()   # Output: Engine stopped.
# # my_car.start_engine()  # Output: Engine started.

# #BANK ACCOUNT
# class BankAccount:
#     def __init__(self, account_number, account_holder, balance=0.0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Successfully deposited ${amount}. New balance: ${self.balance}")
#         else:
#             print("Invalid deposit amount.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew ${amount}. New balance: ${self.balance}")
#         else:
#             print("Insufficient funds or invalid withdrawal amount.")

#     def display_balance(self):
#         print(f"Account Number: {self.account_number}")
#         print(f"Current Balance: ${self.balance}")

# # Creating an instance of the BankAccount class
# my_account = BankAccount("1234567890", "John Doe", 1000.0)

# # Calling methods on the my_account object
# my_account.deposit(500.0)   # Output: Successfully deposited $500. New balance: $1500.0
# my_account.withdraw(200.0)  # Output: Withdrew $200. New balance: $1300.0
# my_account.display_balance()  # Output: Account Number: 1234567890
#                               #         Current Balance: $1300.0
# # Rectangle

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         return self.length * self.width

#     def calculate_perimeter(self):
#         return 2 * (self.length + self.width)

# # Creating an instance of the Rectangle class
# my_rectangle = Rectangle(5, 3)

# # Calculating area and perimeter using the class methods
# area = my_rectangle.calculate_area()
# perimeter = my_rectangle.calculate_perimeter()

# print("Area of the rectangle:", area)
# print("Perimeter of the rectangle:", perimeter)

# # University student
# class Student:
#     def __init__(self,name,year,course) :
#         self.name=name
#         self.year=year
#         self.course=course
        
#     def display_details(self):
#         print("Name", self.name)
#         print("Year",self.year)
#         print("course",self.course)  
        
# my_student =Student("JOJO",3,"BSSE")
# my_student.display_details()

 #EXERCISE 1
 #Calculate area and circumference of a circle       

#   # cirle   
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def calculate_area(self):
#         return 3.14 * self.radius * self.radius
#     def calculate_circumference(self):
#         return 3.14 *2*self.radius 
    
#     #Create object
# my_circle = Circle(7)
# print(my_circle.calculate_area())
# print(my_circle.calculate_circumference)

#exercise 2
#Calculate and dispaly Employes Bonuses (0.5) of salarary(employee:150000,employee2:230000)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self, bonus_rate):
        return self.salary * bonus_rate

# Creating instances of the Employee class for two employees
employee1 = Employee("John", 150000)
employee2 = Employee("Jane", 230000)

# Calculating bonuses using the calculate_bonus() method
bonus_rate = 0.5
bonus1 = employee1.calculate_bonus(bonus_rate)
bonus2 = employee2.calculate_bonus(bonus_rate)

# Displaying the bonuses
print(f"Employee: {employee1.name}\tSalary: ${employee1.salary}\tBonus: ${bonus1}")
print(f"Employee: {employee2.name}\tSalary: ${employee2.salary}\tBonus: ${bonus2}")

     
#ENCAPSULATION
#Example:with a bank account 
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_account_holder(self):
        return self._account_holder

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Successfully deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

# Creating an instance of the BankAccount class
my_account = BankAccount("1234567890", "John Doe", 1000.0)

# Accessing attributes using getter methods
print("Account Number:", my_account.get_account_number())
print("Account Holder:", my_account.get_account_holder())
print("Balance:", my_account.get_balance())

# Calling methods to modify the account balance
my_account.deposit(500.0)   # Output: Successfully deposited $500. New balance: $1500.0
my_account.withdraw(200.0)  # Output: Withdrew $200. New balance: $1300.0
 
print("==========================================================")
#EXAERCISE1
#CONVERT   TEMPRETURE (37)  FROM CELSIUS TO FAHRENRITE    
class TemperatureConverter:
    def __init__(self, temperature):
        self._temperature = temperature

    def celsius_to_fahrenheit(self):
        return (self._temperature * 9/5) + 32

    def get_temperature(self):
        return self._temperature



converter = TemperatureConverter(37)
temperature = converter.get_temperature()
fahrenheit_temp = converter.celsius_to_fahrenheit()

print(f"The temperature {temperature}°C is equal to {fahrenheit_temp}°F.")
print("============================================================")

print("ASSIGNMNENT TWO================================================")
#ASSIGNMENT TWO
#  
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def give_pay_increment(self, increment_amount):
        self._salary += increment_amount


# Create an instance of Employee
employee = Employee("John Doe", 850000)

# Get the employee information
name = employee.get_name()
salary = employee.get_salary()

print(f"Employee Name: {name}")
print(f"Current Salary: {salary}")

# Give a pay increment of 150000
increment_amount = 150000
employee.give_pay_increment(increment_amount)

# Get the updated salary
new_salary = employee.get_salary()

print(f"New Salary: {new_salary}")


print("END===================================")
             


