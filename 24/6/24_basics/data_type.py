import math
# String data type 
 
 # literal assignment 
first ="Dave"
last ="Gray"
 
# print(type(first))
# print(type(first) == str)
# print(isinstance(first,str))

# Constructor function
# pizza = str("Pepperoni")
# print(type(pizza)) 
# print(type(pizza) == str)
# print(isinstance(pizza,str))

# concatenation 
fullname = first + " "+ last 
print(fullname) 

# casting 
decade = str(1980)
print(type(decade))
print ("i like old songs from" + " "+ decade)

print(first.lower())
print(len(first))
first = "    "+first
print(first.strip())

 # build "menu 
title = "menu".upper()
print (title.center(20, "="))
print("coffee".ljust(10,".")+ "$1".rjust(5)) 

# some methods return boolean data
print (first.startswith(" "))
print (first.endswith("e"))
gpa = 45.9
# buildin maths function
print(abs(gpa))
print(abs(gpa * -1))
print (math.pi)
print(math.sqrt(67))
print(math.ceil(gpa))
print(math.floor(gpa))
