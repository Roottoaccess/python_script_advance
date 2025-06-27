# This is the tuple learning script where I will learn about the tuple concepts

# mytuple = ("Max",28,"Boston")
# print(mytuple)

# So iF I write like this then its not a tupple its a string, to make it as a tuple you have to apply , in the last of it....

mytuple1 = ("Maximum")
print(type(mytuple1))

item = tuple(["Max",'56','boston'])
print(item[0])

# Tuple is Immutable.....
# Printing the element using the for loop
for _ in item:
    print(_)
if "Max" in item:
    print("yes")
else:
    print("no")

# Functionality with tupples
t = ('a','p','p','l','e')
print(f'Length of this tuple is: {len(t)}')
print(f"The 'p' present in the tuple is: {t.count('p')}")
print(f'the index number of the "l" is: {t.index("l")}')

# Convert tupple into list
x = list(t)
print(x)
print(f'The type of x is: {type(x)}')
# Slicing concept with tuple
a = (1,2,3,4,5,6,7,8,9,10)
b = a[2:5]; print(b) # slicing in the tuple will not include the first limit but it will include the last limit....

# This is the another way for accesing the tuples and using the concept of unpacking


z = "Max", 24, "boston"
name, age, city = z # Unpacking , but it will only work when there will be the same amount of variables....
print(name); print(age); print(city)

# Advance technique
myty = (0,1,2,3,4)
i1, *i2, i3 = myty

print(i1)
print(i3)
print(i2) # It will converted to list....

import sys
my_list = [0, 1, 2, "hello", True]
mytuple = (0,1,2,"hello",True)

print(f'{sys.getsizeof(my_list)} bytes') # list taking much space
print(f'{sys.getsizeof(mytuple)} bytes') # Tuple is taking less space
# Working with tuple can be eficient than working with list