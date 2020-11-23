# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 14:40:56 2020

@author: Richa Arora
"""
#Files & Lists

# Write a program to prompt for a file name, and then read through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:”pull apart the line to extract the floating-point number on the line.Count these lines and then compute the total of the spam confidence
# values from these lines. When you reach the end of the file, print outthe average spam confidence.

# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745
# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519

#Solution:-

fhand = input("Enter file name:")
fh = open(fhand)
count = 0
total = 0
for line in fh:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        sam = line.find(':')
        gg = line[sam + 1:]
        gg = float(gg)
        total = gg + total
        count = count + 1

print('Average Spam Confidence:', total/count)

#Sometimes when programmers get bored or want to havea bit of fun, they add a harmless Easter Egg to their program Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na booboo”. The program should behave normally for all other files which
#exist and don’t exist. Here is a sample execution of the program:

# python egg.py
# Enter the file name: mbox.txt
# There were 1797 subject lines in mbox.txt
# python egg.py
# Enter the file name: missing.tyxt
# File cannot be opened: missing.tyxt
# python egg.py
# Enter the file name: na na boo boo
# NA NA BOO BOO TO YOU - You have been punk'd!

#Solution:-
fname = input('Enter the file name:  ')
try:
    fhand = open(fname)
except:
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)



#Write a program to read through the mail box data and when you find line that starts with “From”, you will #split the line into words using the split function. We are interested in who sent the
#message, which is the second word on the From line.

# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# You will parse the From line and print out the second word for each From line, then you will also count the number of From (not From:)lines and print out a count at the end. This is a good sample output
# with a few lines removed:

# python fromcount.py
# Enter a file name: mbox-short.txt
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
# zqian@umich.edu
# [...some output removed...]
# ray@media.berkeley.edu
# cwen@iupui.edu
# cwen@iupui.edu
# cwen@iupui.edu
# There were 27 lines in the file with From as the first word

#Solution:-
fhand = open("C:\\Users\\Desktop\\mbox-short.txt") #Add the location of the file
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        line = line.split()
        count = count + 1
        print(line[1])
print('There were', count , 'line in the file with From as the first word')

#OR

fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    else:
        line = line.split()
        line = line[1]
        print(line)
    count += 1
print("There were",count,"lines in the file with From as the first word")


# Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”. Write the program to store the
# numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

# Enter a number: 6
# Enter a number: 2
# Enter a number: 9
# Enter a number: 3
# Enter a number: 5
# Enter a number: done
# Maximum: 9.0
# Minimum: 2.0

#Solution:-
numlist = list()
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
    
    
print('Maximum', max(numlist))
print('Minimum',min(numlist))