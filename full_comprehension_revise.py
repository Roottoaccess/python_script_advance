"""
🔹 List Comprehension Problems
# Create a list of squares for all even numbers from 1 to 50.
# Extract all the vowels from a given string and store them in a list.
# Generate a list of all numbers from 1 to 100 that are divisible by both 3 and 5.
# Convert a list of temperatures in Celsius to Fahrenheit using list comprehension.
# Given a list of integers, create a new list with only the positive numbers, each multiplied by 2.
🔹 Dictionary Comprehension Problems
# Given a list of numbers, create a dictionary where the key is the number and the value is its cube.
# Invert a dictionary: keys become values and values become keys.
# Given a sentence, count the frequency of each word using dictionary comprehension.
Create a dictionary from two lists: one of keys and one of values.
Filter out dictionary items where the value is less than 50.
🔹 Set Comprehension Problems
Create a set of all unique characters in a string that are lowercase letters.
From a list of integers with duplicates, create a set of squares of only the odd numbers.
Create a set of all unique words in a sentence that are longer than 4 characters.
Given a list of strings, create a set of strings that start with a vowel.
Create a set of unique lengths of words in a given paragraph.
"""
# First
x = [i ** 2 for i in range(1,51) if i % 2 == 0]; print(x)
# Second
s = "tony stark is a great scientist"; x1 = [i for i in s if i in ['a','e','i','o','u']]; print(x1)
# Third
x2 = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]; print(x2)
# Forth
celsius_temperatures = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]; x3 = [(i * 9/5) + 32  for i in celsius_temperatures]; print(x3)
# Fifth
y = [2,13,-33,4,-6,8,11,91,-94,101,102]; x4 = [i for i in y if i >= 0 and i % 2 == 0]; print(x4)
# Sixth
y1 = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]; d = {i : i ** 3 for i in y1}; print(d)
# Seventh
d1 = {value:key for key,value in d.items()}; print(d1)
# Eighth
# s1 = "helloworldthisistonystarkyourironman"
# words = s1.split()
# d2 = {word: words.count(word) for word in s1}; print(d2)