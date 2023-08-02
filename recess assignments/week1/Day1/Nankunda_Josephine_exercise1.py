#DAY1 EXERCISE
# use the lens() with the tuple example
My_shops = (1,2,3,4,5,6,7,8,9,10,11,12)
length=len(My_shops)
print ("I have",length," shops in my life")


# Accessing Tuples
accessed= My_shops[4]
print("The shop at index 4 is",accessed)

#sets
#length of sets
my_set = {1, 2, 3, 4, 5}
set_length = len(my_set)
print("The length of the set is:", set_length)

# access elements in a set
my_set = {1, 2, 3, 4, 5}
for element in my_set:
    print(element)


#add items in a set, use the add() method
my_set = {1, 2, 3}
my_set.add(4)
print(" The new set after adding 4 is this " , my_set)  

#Add two sets together

set1 = {1, 2, 3}
set2 = {3, 4, 5}
combined = set1.union(set2)
print(  " The union of the set is this", combined)  

