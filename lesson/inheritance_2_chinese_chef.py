from inheritance_1_chef import Chef

class ChineseChef(Chef):

    def make_fried_rice(self):
        print("The Chinese Chef makes fried rice")

    def make_special_dish(self):
        print("The Chinese Chef makes orange chicken ribs")

'''
 Below is a copy of attributes we want to inherit from inheritance_1_chef.py:

    def make_chicken(self):
        print("The Chinese Chef makes a chicken")

    def make_salad(self):
        print("The Chinese Chef makes a salad")

    def make_special_dish(self):
        print("The Chinese Chef makes orange chicken ribs")
'''

# Note: We do not need to state the commented code within Chinese Chef class, since it is contained
# within the generic chef class, and we already inherit the generic chef attributes, hence we can call
# same content contained within generic chef under the "inheritance_app.py" for ChineseChef
# This is ChineseChef, but we imported generic chef in line 1, then we inherit its attributes in line 3

#Note: where there is a need to use both classes (i.e inherited class and heir class) there can be overlap,
#of function, hence you need to clearly define the function needed for the heir class where necessary.

# Both Chefs make special_dish but that of the generic chef is bbq, while that of the ChineseChef is
#orange chicken ribs, hence, bbq will override orange chicken ribs, except it is otherwise specifically
#declared within the ChineseChef class