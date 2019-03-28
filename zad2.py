# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import cs50 as cs

x = float(input("Input X: "))
y = float(input("Input Y: "))

while x%y != 0 or x % 2 != 0 or y % 2 != 0 :
    print("Wrong numbers, type new ones")
    x = float(input("Input X: "))
    y = float(input("Input Y: "))

print("X: ", x, " Y: ", y)

print("X is divisible by Y") if y!=0 and x % y == 0 else print("X is not divisible by Y")
