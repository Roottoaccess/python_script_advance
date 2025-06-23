# Scripting list in python....
mylist = ['banana','cherry','apple']
print(mylist)
# Accesing the items through indexing
mylist2 = [5, True, "apple",'lill']
print(mylist2[1])

for _ in mylist2:
    print(_)
# Checking from the 
if "apple" in mylist2:
    print(f"yes {"apple"} is present....")
else:
    print(f'No its not present....')

print(f'This is the length of the first list: {len(mylist)}')

mylist.append('lotus'); print(f'This is the list: {mylist} , this is the length of the list: {len(mylist)} now')
# We use insert to insert the element in where ever we want to insert it....
mylist2.insert(1, "blueberry")
print(mylist2)

# Pop function will help to pop the last element from the list....
item = mylist2.pop()
print(f'This is the poped element....')
print(f'This is the list after poping the element: {mylist2}')
# Reverse a list....
mylist2.reverse()
print(mylist2)

unsorted_list = [4,3,1,-1,-5,10]
print(f'This is the unsorted list: {unsorted_list}')

# unsorted_list.sort()
# print(f'This is the sorted list: {unsorted_list}')

# This is the another technique to do this....
sorted_list = sorted(unsorted_list)
print(f'This is the sorted list: {sorted_list}')

# Creating a new list with 5 , 0's
ml = [0] * 5; print(ml)
# Adding the 2 list....
ml1 = [1,2,3,4,5]
n_l = ml + ml1; print(n_l)

# Slicing the list
l = [1,2,3,4,5,6,7,8,9]; a = l[1:5]
print(f'After slicing the list I got: {l}')

# This is to inform that this is a ultimate list python script
print(l[::2]) # steping counter in the list mechanism
list_original = ['banana','cherry','apple','grapes']
# list_copy = list_original.copy()
# list_copy = list(list_original)
list_copy = list_original[:]
list_copy.append('dragon fruit')
print(list_copy)
print(list_original) # This are the three way how we can do the copy of the list without changing the actual list....

# This is the list comprehension....
a = [1,2,3,4,5,6] 
b = [i * i for i in a];print(a); print(b) # This is the list comprehension....

c = [i * i for i in a if i == 4]; print(c)