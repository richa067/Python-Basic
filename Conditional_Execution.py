# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:25:13 2020

@author: Richa Arora
"""
#CONDITIONAL EXECUTION

# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

#Solution:-
try:
    hours = int(input("Enter hours:"))
    rate = float(input("Enter rate:"))
    Pay = 40 * rate + (1.5 * (hours - 40) * rate)
    print("Pay",Pay)
except:
    print("Error,please enter numeric input")
    
    
    
# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

# Score Grade

# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F
# Run the program repeatedly as shown above to test the various different values for
# input.

#Solution:-

score = input(" Enter score:")
try:
    if 0.9 <= float(score) <= 1.0:
        print("A")
    elif 0.8 <= float(score) <=0.9:
        print("B")
    elif 0.7 <= float(score) <= 0.8:
        print("C")
    elif 0.6 <= float(score) <=0.7:
        print("D")
    elif 0.0 <= float(score) <= 0.6:
        print("F")
    else:
        print("Bad Score")

except:
    print("Bad Score")

#Excersice 6 - Chapter 4

def computepay( hours,rate):
    if hours > 40:
        Pay =  40 * rate + (1.5 * (hours - 40) * rate)
    else:
       Pay = hours * rate
    return Pay

hours = float(input("Enter hours:"))
rate = float(input("Enter rate:"))   

payment = computepay(hours,rate)
print("Pay",payment)

#Excersice 7 - Chapter 4

score = input(("Enter score:"))
def computegrade(score):
    try:
        if 0.9 <= float(score) and float(score) <= 1.0:
            grade =("A")
        elif 0.8 <= float(score) and float(score) <=0.9:
            grade =("B")
        elif 0.7 <= float(score) and float(score) <= 0.8:
            grade =("C")
        elif 0.6 <= float(score) and float(score) <=0.7:
            grade =("D")
        elif 0.0 <= float(score) and float(score) <= 0.6:
            grade =("F")
        return grade
        
    except:
        grade =("Bad Score")
        return grade
        

x = computegrade(score)
print(x)