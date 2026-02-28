# python learn.py
# name = "sadiq"
# age = 22
# print(name, age)

# data types
# String 
# integer
# float
# boolean
# list
# dictionary


#funtions
# def greet(name):
#     return "hello " + name
# print(greet("sadiq"))

#if condition 
# age = 22
# if age < 18:
#     print("your are a lil brat boiiiii")
# else:
#     print("welcome to the reality check boiiii")



#loops 
# n = 5
# for i in range(n):
#     print(i)


# regualr expressions
# import re 

# text = "12345"
# pattern = r'^\d{5}$' #matches one or more digits from start to end

# if re.match(pattern, text):
#     print("match found")
# else: 
#     print("no match found")


import re

# The Pattern Breakdown:
# ^      -> Start of string
# (\w+)? -> Optional word characters (0 or 1 time)
# \d{3}  -> Exactly 3 digits
# .      -> Any single character (except newline)
# \w+    -> 1 or more word characters
# \s+    -> 1 or more whitespace characters
# .      -> One final character
# $      -> End of string

pattern = r"^(\w+)?\d{3}.?\w+\s+.$"
test_string = "ID123-Data  !"

if re.match(pattern, test_string):
    print("Match successful!")
else:
    print("No match found.")