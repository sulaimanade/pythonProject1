#LISTS. working with lists
#Lists helps us to work with large set of data, it helps us to store multiple values into a List, variable stores a single value.
friends = ["Adam", "Saheed", 20, "Sumayyah", "Mustapha", True] #Lists accepts values of different types
print(friends)

#UPDATE LIST
fruits = ["Lemon", "Mango", "Orange", "Guava"]
fruits[0] = "Apple" #values in a List can be updated to modify its content, lemon is been changed to apple here.
print(fruits)

#APPEND TO LIST
foods = ["Yam", "Rice","Beans", "Potatoe"] #using .append
foods.append("Spaghetti") #adding another value to an existing list, note that this will add the new value to end of list.
print(foods)

#INSERT TO LIST
foods = ["Yam", "Rice","Beans", "Potatoe"] #using .insert
foods.insert(1,"Spaghetti") #adding another value to an existing list, here we specify the position to add the new value.
print(foods)

#REMOVE FROM LIST
foods = ["Yam", "Rice","Beans", "Potatoe"] #using .remove
foods.remove("Beans") #removing a value from an existing list.
print(foods)

#EXTEND LIST
Pupils = ["Adam", "Wale","Ade", "Mike"]
Girls = ["Maryam", "Shade", "Cynthia"]
Pupils.extend(Girls) #the .extend helps to add a list to another list.
print(Pupils)

#CELAR LIST VALUE
students = ["Sodiq", "Sam","Smith", "Abu"]
print(students)
students.clear() #the .clear helps to clear all values within a list
print(students)

#POP LIST VALUE
flavor = ["Vanila", "Chocolate","Strawberry", "Banana"]
flavor.pop() #with .pop we can pop out (delete) the last value in a list
print(flavor)

#INDEX
flavor = ["Vanila", "Chocolate","Strawberry", "Banana"]
print(flavor.index("Banana")) #this returns the index number of the specified value Banana from the list

#COUNT LIST VALUE
my_flavor = ["Vanila", "Chocolate","Strawberry", "Banana", "Vanila"]
print(my_flavor.count("Vanila"))

#SORT LIST VALUE
my_flavor = ["Vanila", "Chocolate","Strawberry", "Banana", "Vanila"]
test_result = [89, 67, 93, 80, 87,70,89]
my_flavor.sort() #this helps to sort the list values in order
test_result.sort() #this helps to sort the list values in order
print(my_flavor)
print(test_result)

#REVERSE SORT ORDER
my_flavor = ["Vanila", "Chocolate","Strawberry", "Banana", "Vanila"]
test_result = [89, 67, 45, 50, 35,70,90]
my_flavor.reverse() #this creates a reverse order of the list values
test_result.reverse() #this creates a reverse order of the list values
print(my_flavor)
print(test_result)

#COPY FROM A LIST TO ANOTHER
my_flavor = ["Vanila", "Chocolate","Strawberry", "Banana", "Vanila"]
my_flavor2 = my_flavor.copy() #this helps to copy all values another list
print(my_flavor2)
