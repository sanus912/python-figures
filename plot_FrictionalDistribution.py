#!/opt/local/bin/python2.7
#coding=utf-8
import scipy
from scipy import interpolate, constants
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import string
import sys, os

from matplotlib import rc, rcParams

rc('text',usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern Roman']})
rc('axes', linewidth=1.5)

in_file = open('fitting_3D.txt',"r")


points = []
values = []

x_min = 0
x_max = 4
y_min = 0
y_max = 4
dx=0.005
dy=dx

for line in in_file:
    line=string.split(line)
    if len(line) > 1:
        points.append([line[0], line[1]])
        values.append(line[2])

P_of_f = scipy.interpolate.LinearNDInterpolator(points, values,0)

X,Y=np.meshgrid(np.arange(x_min, x_max, dx), np.arange(y_min, y_max, dy))
Z=P_of_f(X,Y)


xshift=0.02
yshift=0.02
plt.tick_params(labelsize=20)
ticks_locations = np.arange(0,5,1)
ticks_labels = [r'$'+str(t)+'$' for t in ticks_locations]

#cheat a bit with the axes to avoid a small white gap between map and axis
xticks_locations = list(ticks_locations)
xticks_locations[0] += xshift
xticks_locations[-1] -= xshift
yticks_locations = list(ticks_locations)
yticks_locations[0] += yshift
yticks_locations[-1] -= 2*yshift

plt.yticks(yticks_locations, ticks_labels)
plt.xticks(xticks_locations, ticks_labels)
plt.xlabel(r'\textbf{$f^{\,n}/\langle f^{\,n}\rangle$}', size=25)
plt.ylabel(r'\textbf{$f^{\,t}/\langle f^{\,t}\rangle$}', size=25)
plt.axis([x_min+xshift, x_max-xshift, y_min+yshift, y_max-2*yshift])

plt.pcolormesh(X, Y , Z+0.000000001, cmap=matplotlib.cm.jet, norm = matplotlib.colors.LogNorm(), vmin=0.01,vmax=0.5)

plt.text(2.8,3.9,r'\textbf{3D($\mu=\infty$)}',size=20,color='white',va='top')
plt.text(1.05,4.2,r'\textbf{empirical formula[39]}',size=20,color='black',va='top')
plt.text(-0.5,4,r'\textbf{(E)}',size=20,color='black',va='top')

cbar_ticks = [ 0.01, 0.02, 0.05, 0.1, 0.2, 0.5]
cbar_labels = [r'$'+str(t)+'$' for t in cbar_ticks]
cbar = plt.colorbar()
cbar.set_ticks(cbar_ticks)
cbar.set_ticklabels(cbar_labels)
cbar.ax.tick_params(labelsize=20)

plt.savefig('P_of_F.png', format="png", dpi=300, close=True, verbose=True, bbox_inches='tight')
#plt.show()

