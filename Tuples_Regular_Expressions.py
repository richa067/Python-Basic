# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 17:38:18 2020

@author: Richa Arora
"""


#Tuples

# This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using
# the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

#Solution:-
fname = input('Enter the file name:')
fhand = open(fname)
counts = dict()
for line in fhand:
    words = line.rstrip().split()
    if line.startswith("From "):
        words = words[5]
        #print(words)
        words = words[0:2]
        print(words)
        counts[words] = counts.get(words,0) + 1

lst = list()
print( sorted( [ (k,v) for k,v in counts.items() ] ) )

#Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should
#not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from #several different languages and see how letter frequency varies between languages. Compare your results with
#the tables at https://wikipedia.org/wiki/Letter_frequencies.

#Solution:-

import string

fname = input('Enter file name: ')
try:
	fhandle = open(fname)
except:
	print ('File cannot be opened:', fname)
	exit()
letters = dict()
for line in fhandle:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower().split()
    for t in line:
        word = list(t)
        for letter in word:
            letters[letter] = letters.get(letter,0) + 1

lst= []
print( sorted( [ (k,v) for k,v in letters.items() ] ) )

# Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

# $ python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author
# $ python grep.py
# Enter a regular expression: ^Xmbox.
# txt had 14368 lines that matched ^X-
# $ python grep.py
# Enter a regular expression: java$
# mbox.txt had 4175 lines that matched java$

#Solution:-

import re

x = input('Enter a regular Expression:')
fhand = open('C:\\Users\\Piyush Raj\\Desktop\\mbox.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if re.search(x, line):
        count = count + 1
        # print(line)

print('There are', count, 'number of lines')


# Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

# $ python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author
# $ python grep.py
# Enter a regular expression: ^Xmbox.
# txt had 14368 lines that matched ^X-
# $ python grep.py
# Enter a regular expression: java$
# mbox.txt had 4175 lines that matched java$

#Solution:-

import re
hand = open('C:\\Users\\Desktop\\mbox-short.txt')  # or mbox-short.txt #Enter the file path
count = 0
Total = 0
for line in hand:
    line = line.rstrip()
    x = re.findall('New Revision: ([0-9.]+)', line)
    if len(x) > 0:
        Total = float(x[0]) + Total
        count = count + 1
        print(x)
# print('There are', count, 'number of lines')
print(count)
print(Total)
print('Average:', Total/count)

