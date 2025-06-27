# This script is for understanding the dictionary in python
# Dictionary: key-value pairs, Unordered, Mutable

mydict = {
    "name": "Max",
    "Age": 28,
    "city": "New York"
}; print(mydict)
# This is the another method to declare dictionary
mydict2 = dict(name="Mary", age = 28, city = "boston")
print(mydict2)
value =mydict["name"]; print(value)
# Adding a key and value in the dictionary....
mydict['email'] = 'abcd@gmail.com'; print(mydict)
# For deleting from the dictionary
del mydict['name']; print(mydict)

try:
    print(mydict['name'])
except:
    print('name is not present now !')
# looping through the keys
# for key in mydict.keys():
#     print(key)
# looping through the values
# for value in mydict.values():
#     print(value)

# I can print both key and value at the same time by using the loops in this way
for key,value in mydict.items():
    print(key,value)

# Copying the dictionary
print(mydict)
my_dict_copy = mydict
print(my_dict_copy) # If I update it it will also change in the actual one
# Actual copy we can use this one
# my_dict_copy = mydict.copy()

# There is update function , will update othe missing key and values from the another dictionary....
# mydict.update(my_dict_2); print(mydict)
my_dict2 = {"name":"Maxx","age":28,"email":"max@gmail.com"}; print(my_dict2)

x_y = {3:9, 6:36, 9:81}; print(x_y)
# We can also create a dictionary by have the tuple value as the key....
mytuple = (8,7)
my_dic = {mytuple:15}; print(my_dic) 
# Tuple is possible for the but list is not possible....