input_string = "Bhoomi"
dictionary = {x : input_string.count(x) for x in set(input_string)} 
 
print(dictionary)