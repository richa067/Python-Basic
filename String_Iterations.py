# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:48:35 2020

@author: Richa Arora

"""

#Iterations & Strings:-

# Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print outthe total, count, and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error message and skip to the next number.

# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333
# count = 0
# total = 0

#Solution:-

while True:
  try:
    line = input('Enter an integer: ')
    if line == 'done':
      break
    x = float(line)
  except:
    print("Invalid Input")
    continue
  count = count + 1
  total = total + x

print( total, count, total / count)

#Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

#Solution:-
largest = None
smallest = None
while True:
    try:
        line = input('Enter an Integer:')
        if line == 'done':
            break
        x = float(line)
        if largest is None or x > largest:
            largest = x
        if smallest is None or x < smallest:
            smallest = x
    except:
        print('Invalid Input')


print(largest,smallest)

# Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

#Solution:-

word = "banana"
get = "a"
word.count(get)
print(word.count(get))

# or 

word = 'banana'
#for letter in word:
new = word.count('a')
print(new)


# Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

#Solution:-

str = 'X-DSPAM-Confidence:0.8475'

s = str.find(":")
h = str[s+1:]
h = float(h)
print(h)

#OR

str = 'X-DSPAM-Confidence:0.8475'

s = str.find(":")
g = len(str)
h = str[s+1:g]
k = float(h)
print(h)
print(k)



