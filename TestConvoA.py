# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 22:57:25 2020

@author: Lucas
"""
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from ConvoA import *

N = 100
T = 1/N
fs = 1/T
t = np.arange(-5, 5, T)
f = 5
y = np.concatenate((np.zeros(300), np.ones(400), np.zeros(300)))
z = np.exp(t)/15


ConvoA(z, y, t, T, 25)
