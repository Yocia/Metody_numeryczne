# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:09:25 2019

@author: Julia
"""

from math import pi

x = float(input("Please enter first circle radius: "));
y = float(input("Please enter second circle radius: "));

while x <= 0:
    x = float(input("This radius is smaller than 0, please enter another one."));
while y <= 0:
    y = float(input("This radius is smaller than 0, please enter another one."));

print("Perimeter of first circle: ", 2*x*pi)
print("Perimeter of the second circle: ", 2*y*pi)
print("Field of the first circle: ", pi*x**2)
print("Field of the second circle: ", pi*y**2)