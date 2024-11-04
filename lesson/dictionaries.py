#ike a list, a dictionary is a mutable collection of many values. But unlike
#indexes for lists, indexes for dictionaries can use many different data types,
#not just integers. Indexes for dictionaries are called keys, and a key with its
#associated value is called a key-value pair.

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    100: "OneHundred"
}


print(monthConversions["Nov"])
print(monthConversions[100])


#This assigns a dictionary to the myCar variable. This dictionary’s keys are
#'size', 'color', and 'disposition'. The values for these keys are 'fat', 'gray',
#and 'loud', respectively. You can access these values through their keys:
myCar = {"brand": "Toyota", "color": "white", "type": "suv"}

print(myCar["color"])
