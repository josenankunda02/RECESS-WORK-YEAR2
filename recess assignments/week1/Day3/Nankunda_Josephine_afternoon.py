#INDIVIDUL ASSIGNMENT
#LISTS
#  1. Create a list with 5 items (names of people) and write a python program to output the 2nd
# item
names = ["John", "Emily", "Michael", "Sophia", "David"]
second_item = names[1]
print(second_item)

# 2.Write a python program to change the value of the first item to a new value
names = ["John", "Emily", "Michael", "Sophia", "David"]
new_value = "Alex"
names[0] = new_value
print(names)

# 3.Write a python program to add a sixth item to the list
names = ["John", "Emily", "Michael", "Sophia", "David"]
new_item = "Olivia"
names.append(new_item)
print(names)
#4. Write a python program to add “Bathel” as the 3rd item in your list
names = ["John", "Emily", "Michael", "Sophia", "David"]
new_item = "Bathel"
names.insert(2, new_item)
print(names)

#5. Write a python program to remove the 4th item from the list
names = ["John", "Emily", "Michael", "Sophia", "David"]
removed_item = names.pop(3)
print(names)

#6. Use negative indexing to print the last item in your list
names = ["John", "Emily", "Michael", "Sophia", "David"]
last_item = names[-1]
print(last_item)
#7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
items = ["Apple", "Banana", "Orange", "Grapes", "Mango", "Pineapple", "Strawberry"]

for i in range(2, 5):
    print(items[i])
# 8. Write a list of countries and make a copy of it.
countries = ["United States", "Canada", "Germany", "Australia", "Japan"]
countries_copy = countries.copy()

# 9. Write a python program to loop through the list of countries
countries = ["United States", "Canada", "Germany", "Australia", "Japan"]

for country in countries:
    print(country)

# 10. Write a list of animal names and sort them in both descending and ascending order.
animal_names = ["Lion", "Elephant", "Tiger", "Giraffe", "Zebra"]
ascending_order = sorted(animal_names)
descending_order = sorted(animal_names, reverse=True)

print("Ascending order:", ascending_order)
print("Descending order:", descending_order)

# 11. Using the list above, write a python program to output only animal names with the letter
# ‘a’ in them
animal_names = ["Lion", "Elephant", "Tiger", "Giraffe", "Zebra"]

for name in animal_names:
    if 'a' in name.lower():
        print(name)

# 12. Write two lists, one containing your first names and the other your second names. Join
# the two lists.
first_names = ["Nankunda"]
last_names = ["Josephine"]

full_names = [first + " " + last for first, last in zip(first_names, last_names)]

print(full_names)

#Exercise2 (Tuples)
# 1. Consider the tuple below;
# x = (“samsung”, “iphone”, “tecno”, “redmi”)
# Write a python program to output your favorite phone brand.
x = ("samsung", "iphone", "tecno", "redmi")
Brand_liked = x[2]
print(Brand_liked)

# 2. Use negative indexing to print the 2nd last item in your tuple.
x = ("samsung", "iphone", "tecno", "redmi")
second_last_item = x[-2]
print(second_last_item)

# 3. Using the phones list above, write a python program to update “iphone” to “itel”
x = ("samsung", "iphone", "tecno", "redmi")
x = list(x)
x[x.index("iphone")] = "itel"
x = tuple(x)
print(x)


# 4. Write a python program to add “Huawei” to your tuple.
x = ("samsung", "iphone", "tecno", "redmi")
x = x + ("Huawei",)
print(x)

# 5. Write a python program to loop through the tuple above.
x = ("samsung", "iphone", "tecno", "redmi")
for item in x:
    print(item)

# 6. Write a python program to remove/delete the first item in your tuple.
x = ("samsung", "iphone", "tecno", "redmi")
x = x[1:]
print(x)

# 7. Using the tuple() constructor, create a tuple of the cities in Uganda.
cities = tuple(["Kampala", "Entebbe", "Jinja", "Gulu"])
print(cities)

# 8. Write a python program to unpack your tuple.
x = ("samsung", "iphone", "tecno", "redmi")
brand1, brand2, brand3, brand4 = x
print(brand1, brand2, brand3, brand4)

# 9. Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
cities = ("Kampala", "Entebbe", "Jinja", "Gulu")
for i in range(1, 4):
    print(cities[i])

# 10. Write two tuples, one containing your first names and the other your second names. Join
# the two tuples.
first_names = ("NANKUNDA")
last_names = ("JOSEPHINE")
full_names = first_names + last_names
print(full_names)

# 11. Create a tuple of colors and multiply it by 3.
colors = ("red", "green", "blue")
multiplied_colors = colors * 3
print(multiplied_colors)

# 12. Return the number of times 8 appears in this tuple
# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_of_eight = thistuple.count(8)
print(count_of_eight)


# Exercise3 (Sets)

# 1. Use the set() constructor to create a set of 3 of your favorite beverages.
beverages = set(["coffee", "tea", "juice"])
print(beverages)

# 2. Use the correct method to add 2 more items to the beverages set.
beverages = set(["coffee", "tea", "juice"])
beverages.add("water")
beverages.add("soda")
print(beverages)

# 3. Given the set below;
# mySet = {“oven”, “kettle”, “microwave”, “refrigerator”}
# Check if microwave is present in the set.
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set.")
else:
    print("Microwave is not present in the set.")

# 4. Write a python program to remove “kettle” from the set above.
mySet = {"oven", "kettle", "microwave", "refrigerator"}
mySet.remove("kettle")
print(mySet)

# 5. Write a python program to loop through the set above.
mySet = {"oven", "kettle", "microwave", "refrigerator"}
for item in mySet:
    print(item)

# 6. Write a set of 4 items and a list of two items. Write a python program to add elements in
# the list to elements in the set.
mySet = {1, 2, 3, 4}
myList = [5, 6]
mySet.update(myList)
print(mySet)

# 7. Write two sets, one containing your ages and the other your first names. Join the two
# sets.
ages = {21}
first_names = {"JOSEPHINE"}
joined_set = ages.union(first_names)
print(joined_set)

# Exercise4 (Strings)
# 1. Declare two variables, an integer and a string and use the correct method to concatenate
# the two variables.

integer = 10
string = " years old"
concatenated = str(integer) + string
print(concatenated)

# 2. Consider the example below;
# txt = “ Hello, Uganda! ”
# Output the string without spaces at the beginning, in the middle and at the end.
txt = " Hello, Uganda! "
without_spaces = txt.strip()
print(without_spaces)

# 3. Write a python program to convert the value of ‘txt’ to uppercase.
txt = "Hello, Uganda!"
uppercase_txt = txt.upper()
print(uppercase_txt)

# 4. Write a python program to replace character ‘U’ with ‘V’ in the string above.
txt = "Hello, Uganda!"
replaced_txt = txt.replace("U", "V")
print(replaced_txt)

# 5. Using the code below, write a python program to return a range of characters in the 2nd , 3rd and 4th position.
# y = “I am proudly Ugandan”
y = "I am proudly Ugandan"
range_of_characters = y[1:4]
print(range_of_characters)

# 6. The piece of code below will give an error when output;
# x = “All “Data Scientists” are cool!”
# Write a python program to correct it.
x = 'All "Data Scientists" are cool!'
print(x)


# Exercise5 (Dictionaries)
# 1. With reference to the dictionary below, write a python program to print the value of the shoe size.
# Add this dictionary to your .py file
# Shoes = {
# “brand” : “Nick”,
# “color” : “black”,
# “size” : 40
# }
Shoes = {"brand": "Nick", "color": "black", "size": 40}
shoe_size = Shoes["size"]
print(shoe_size)

# 2. Write a python program to change the value “Nick” to “Adidas”
Shoes = {"brand": "Nick", "color": "black", "size": 40}
Shoes["brand"] = "Adidas"
print(Shoes)

# 3. Write a python program to add a key/value pair "type”: "sneakers" to the dictionary
Shoes = {"brand": "Nick", "color": "black", "size": 40}
Shoes["type"] = "sneakers"
print(Shoes)

# 4. Write a python program to return a list of all the keys in the dictionary above.
Shoes = {"brand": "Nick", "color": "black", "size": 40}
keys_list = list(Shoes.keys())
print(keys_list)

# 5. Write a python program to return a list of all the values in the dictionary above.
Shoes = {"brand": "Nick", "color": "black", "size": 40}
values_list = list(Shoes.values())
print(values_list)

# 6. Check if the key “size” exists in the dictionary above.
Shoes = {"brand": "Nick", "color": "black", "size": 40}
if "size" in Shoes:
    print("Key 'size' exists in the dictionary.")
else:
    print("Key 'size' does not exist in the dictionary.")

# 7. Write a python program to loop through the dictionary above.
Shoes = {"brand": "Nick", "color": "black", "size": 40}
for key, value in Shoes.items():
    print(key, ":", value)

# 8. Write a python program to remove “color” from the dictionary.
Shoes = {"brand": "Nick", "color": "black", "size": 40}
del Shoes["color"]
print(Shoes)

# 9. Write a python program to empty the dictionary above.
Shoes = {"brand": "Nick", "color": "black", "size": 40}
Shoes.clear()
print(Shoes)

# 10. Write a dictionary of your choice and make a copy of it.
original_dict = {"key1": "value1", "key2": "value2"}
copy_dict = original_dict.copy()
print(copy_dict)

# 11. Write a python program to show nested dictionaries
person = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    }
}

print(person)
