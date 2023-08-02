#INheritance
# Exercise
# Calculate area and perimeter of a circle and a rectangle

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

circle = Circle(5)
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

rectangle = Rectangle(4, 6)
print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())

#Multiple Inheritance
class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print("Color:", self.color)


class Area:
    def calculate_area(self):
        pass


class Perimeter:
    def calculate_perimeter(self):
        pass


class Rectangle(Shape, Area, Perimeter):
    def __init__(self, color, length, width):
        Shape.__init__(self, color)
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

rectangle = Rectangle("Red", 4, 6)
print("Rectangle color:", rectangle.color)
print("Rectangle area:", rectangle.calculate_area())
print("Rectangle perimeter:", rectangle.calculate_perimeter())


#Method Overriding
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass


class Cat(Animal):
    def sound(self):
        return "Meow"


class Dog(Animal):
    def sound(self):
        return "Woof"


# Create instances of the subclasses
cat = Cat("Whiskers")
dog = Dog("Buddy")

# Call the sound method on the instances
print(cat.name + " says:", cat.sound())
print(dog.name + " says:", dog.sound())

#Polymorphism
#Method overriding
#method overloading
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Create instances of the subclasses
circle = Circle(5)
rectangle = Rectangle(4, 6)



# Iterate over the shapes and call their area and perimeter methods

# print("Area:", circle.area())
# print("Perimeter:", rectangle.perimeter())
    
# #Overloading

# class Animal:
#     def _add(self, name,breed):
#        return name + breed

#     def add(self,name,breed,total):
#         return name+breed+total
# animal = Animal()
# print(Animal.add(2,4) )
# print(Animal._add(5,9,8) )   
    
    
# Abstruction
#Allows you to focus on esssential futures and hide them from uncesssary details
# Python program demonstrate  
# abstract base class work   
from abc import ABC, abstractmethod   
class Car(ABC):   
    def mileage(self):   
        pass  
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):   
            print("The mileage is 27kmph ")   
          
# Driver code   
t= Tesla ()   
t.mileage()   
  
r = Renault()   
r.mileage()   
  
s = Suzuki()   
s.mileage()   
d = Duster()   
d.mileage()  

    # ASSIGNMENT
      # CREATE A RECEIT PROGRAM WITH GUI INTERFACE
      
import tkinter as tk

class ReceiptProgram:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("RECEIT PROGRAM")

        # Create labels and entry fields
        self.label_item = tk.Label(self.window, text="Item:")
        self.entry_item = tk.Entry(self.window)

        self.label_price = tk.Label(self.window, text="Price:")
        self.entry_price = tk.Entry(self.window)

        self.label_quantity = tk.Label(self.window, text="Quantity:")
        self.entry_quantity = tk.Entry(self.window)

        self.label_total = tk.Label(self.window, text="Total:")

        # Create the button
        self.button_add = tk.Button(self.window, text="Add Item", command=self.add_item)

        # Create the text box
        self.text_box = tk.Text(self.window, height=10, width=40)
        self.text_box.config(bg="green")
        # Layout the labels, entry fields, button, and text box
        self.label_item.grid(row=0, column=0)
        self.entry_item.grid(row=0, column=1)

        self.label_price.grid(row=1, column=0)
        self.entry_price.grid(row=1, column=1)

        self.label_quantity.grid(row=2, column=0)
        self.entry_quantity.grid(row=2, column=1)

        self.label_total.grid(row=3, column=0, sticky="W")

        self.button_add.grid(row=4, column=0, columnspan=2)

        self.text_box.grid(row=5, column=0, columnspan=2)

        # Initialize the total variable
        self.total = 0

    def add_item(self):
        item = self.entry_item.get()
        price = float(self.entry_price.get())
        quantity = int(self.entry_quantity.get())

        line_total = price * quantity
        self.total += line_total

        receipt_line = f"{item} - {price} x {quantity} = {line_total}\n"

        self.text_box.insert(tk.END, receipt_line, "receipt")  # Apply the "receipt" tag to the receipt text
        self.entry_item.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)

        self.label_total.config(text="Total: " + str(self.total))

    def run(self):
        self.window.mainloop()

# Create an instance of the ReceiptProgram class and run the program
receipt_program = ReceiptProgram()
receipt_program.run()





                       
            