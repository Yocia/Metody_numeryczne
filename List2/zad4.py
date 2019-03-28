# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:53:02 2019

@author: Julia
"""

#import decimal as de

x = float(input("Input X: "))
y = float(input("Input Y: "))

while y == 0:
    y = float(input("Y = 0, input new Y: "))

print(round(x/y, 2))