# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 22:18:33 2020

@author: Richa Arora

"""

#Dictionaries

# Add code to the above program to figure out who has the most messages in the file. After all the data has beenread and the dictionary has been created, look through the dictionary using a maximum
# loop to find who has the most messages and print how many messages the person has.

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195

#Solution:-

fname = input('Enter the file name:')
fhand = open(fname)
counts = dict()
for line in fhand:
    words = line.rstrip().split()
    if line.startswith("From "):
        words = words[1]
        counts[words] = counts.get(words,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigword is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword,bigcount)


#OR

hand = open('C:\\Users\\Piyush Raj\\Desktop\\mbox-short.txt')
counts = dict()
for line in hand:
    if line.startswith("From "):
        words = line.strip().split()
        day = words[1]
        if day not in counts:
            counts[day] = 1
        else:
            counts[day] += 1
print(counts)


largest = None
for itervar in counts:
    if largest is None or counts[itervar] > largest :
        largest = counts[itervar]
        sender = itervar
print('Largest:', largest, sender)


# This program records the domain name (instead of theaddress) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.

# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

#Solution:-
name = input('Enter the file name:')
fhand = open(name)
counts = dict()
for line in fhand:
    words = line.rstrip().split()
    if line.startswith("From "):
        words = words[1]
        k = words.split("@")[1]
        counts[k] = counts.get(k,0) + 1

print(counts)


#OR

hand = open('mbox-short.txt')
counts = dict()
for line in hand:
    if line.startswith("From"):
        words = line.rstrip().split()
        email = words[1]
        domain = email.split("@")[1]
        counts[domain] = counts.get(domain,0) + 1
        # if day not in counts:
        #     counts[day] = 1
        # else:
        #     counts[day] += 1
print(counts)       