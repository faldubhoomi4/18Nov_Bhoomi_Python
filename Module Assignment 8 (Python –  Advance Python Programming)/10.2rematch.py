import re

mystr = "My name is bhoomi" 

a = re.match("bhoomi", mystr)
b = re.match("test", mystr)
print(a)
print(b)