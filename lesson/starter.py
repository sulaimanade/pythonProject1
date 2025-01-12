














#LISTS. working with lists
#Lists helps us to work with large set of data, it helps us to store multiple values into a List, variable stores a single value.
friends = ["Adam", "Saheed", 20, "Sumayyah", "Mustapha", True] #Lists accepts values of different types
print(friends)

fruits = ["Lemon", "Mango", "Orange", "Guava"]
fruits[0] = "Apple" #values in a List can be updated to modify its content, lemon is been changed to apple here.
print(fruits)

foods = ["Yam", "Rice","Beans", "Potatoe"] #using .append
foods.append("Spaghetti") #adding another value to an existing list, note that this will add the new value to end of list.
print(foods)

foods = ["Yam", "Rice","Beans", "Potatoe"] #using .insert
foods.insert(1,"Spaghetti") #adding another value to an existing list, here we specify the position to add the new value.
print(foods)

foods = ["Yam", "Rice","Beans", "Potatoe"] #using .remove
foods.remove("Beans") #removing a value from an existing list.
print(foods)


Pupils = ["Adam", "Wale","Ade", "Mike"]
Girls = ["Maryam", "Shade", "Cynthia"]
Pupils.extend(Girls) #the .extend helps to add a list to another list.
print(Pupils)


students = ["Sodiq", "Sam","Smith", "Abu"]
print(students)
students.clear() #the .clear helps to clear all values within a list
print(students)

flavor = ["Vanila", "Chocolate","Strawberry", "Banana"]
flavor.pop() #with .pop we can pop out the last value in a list
print(flavor)

flavor = ["Vanila", "Chocolate","Strawberry", "Banana"]
print(flavor.index("Banana")) #this returns the index number of the specified value Banana from the list

my_flavor = ["Vanila", "Chocolate","Strawberry", "Banana", "Vanila"]
print(my_flavor.count("Vanila"))

my_flavor = ["Vanila", "Chocolate","Strawberry", "Banana", "Vanila"]
my_flavor.sort()
print(my_flavor)

just_numbers = [2, 4,1,2,8,45,86]
just_numbers.sort()
print(just_numbers)

just_numbers = [2,4,1,2,8,45,86]
just_numbers.reverse()
print(just_numbers)