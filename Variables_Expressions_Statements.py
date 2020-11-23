# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 17:49:13 2020

@author: Richa Arora
"""
#Variables, Expressions and Statements

#Write a program to prompt the user for hours and rate per hour to compute gross pay.
Hours = input('Enter Hours:')
Rate = input('Enter Rate:')
Pay = float(Hours)* float(Rate)
print('Pay:', Pay)




#Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and #print out the converted temperature.
celsius = float(input('Enter degrees in Celsius:'))
fahrenheit = float(celsius * 9/5 + 32)
print (celsius, ('degrees Celsius equals'), fahrenheit, ('degrees Fahrenheit'))