# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 14:57:02 2022

@author: seoil
"""

import numpy as np
import random
import matplotlib.pyplot as plt

a = np.random.random([2,3])
b = np.random.random([2,3])

print (a)
print (b)
print(a+b)
print(a-b)

e= np.matmul(a,b.T)
print(e)
print(a/b)
 
x= np.array([1,2,3,4,5,6])
ya= a.reshape(6,1)
yb= b.reshape(6,1)

plt.plot(x,ya[:,0],'yo--',linewidth=1.5,markersize=8)
plt.plot(x,yb[:,0],'co--',linewidth=1.5,markersize=8)

plt.xlabel('X')
plt.ylabel('Y_Random')
plt.title('201807558 KDH')
plt.legend(['a', 'b'])
plt.grid()
plt.show()
