#!/opt/local/bin/python2.7
#coding=utf-8
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0,4.0,0.005)
y = np.arange(0.0,4.0,0.005)
plt.pcolormesh(x, y , x*x+y*y+0.000000001)
plt.savefig('test1.png')