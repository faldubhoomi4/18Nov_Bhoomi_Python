import re

mystr = "My name is bhoomi" 

a = re.search("bhoomi", mystr)
b = re.search("test", mystr)
print(a)
print(b)