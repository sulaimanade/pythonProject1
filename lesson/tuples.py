#TUPLES
#Tuple is immutable, the values in a tuple can't be changed once created
#You'll store a data inside a tuple when the data doesn't need to be mutable
#Values in a Tuple are called using their index number (i.e position)
#A good use of tuple is to store coordinates

coordinates = (4, 7)
print(coordinates[1]) #specify the index of value to be called using square bracket.

#Tuple values cannot be changed
coordinates[0] = 2 #here, we try to replace 4 with 2
print(coordinates[0]) #python will throw an error
