# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:03:40 2019

@author: Julia
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def wave(x):
    x_knots = np.linspace(-x*np.pi,x*np.pi,201)
    y_knots = np.linspace(-x*np.pi,x*np.pi,201)
    X, Y = np.meshgrid(x_knots, y_knots)
    R = np.sqrt(X**2+Y**2)
    Z = np.cos(R)**2*np.exp(-0.1*R)
    ax = Axes3D(plt.figure(figsize=(8,5)))
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
    plt.show()

wave(float(input("Input X:")))
