# You can read files directly from local drive using the "Open" function
# specify the file name or directory plus file name
# You can use Absolute path, Relative path, or just the file name.
# There are several modes with which you can have a file open: "r"= read, "w"= write, "a"= append, "r+"= read and write

#student_file = open("student name.txt", "r")

#print(student_file.readable()) #this helps to confirm if the file is readable or not
#print(student_file.read()) #reads all content of the file
#print(student_file.readline()) #reads a line (row) from content of the file
#print(student_file.readline()) #if you run it second time, it reads second line (row) from content of the file and so on...
#print(student_file.readlines()) #this reads all records in our data and put them in an array

student_file = open("student name.txt", "r")
#for student in student_file.readlines():
#    print(student)

print(student_file.readlines()[0]) # read to access a specific line using index

#print(student_file.readlines())
student_file.close() #this closes the file when you're done reading it.
