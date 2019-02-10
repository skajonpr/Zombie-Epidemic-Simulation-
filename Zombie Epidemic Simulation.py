# -*- coding: utf-8 -*-
"""
@author: Sukit Kajonpradapkul

Description: The program is to simulate the rise of number of zombie epidemic.

"""
import numpy as np
import matplotlib.pyplot as plt

def z(t):     
    return ((8.*H[t]*Z[t])/(1.6*(10**6)))-(2.*Z[t])

def h(t):
    return -((8.*H[t]*Z[t])/(1.6*(10**6)))

def r(t):
    return 2.*Z[t]


delta_t = 0.1
num_steps = int(28./delta_t)

Z = np.zeros(num_steps+1)
H = np.zeros(num_steps+1)
R = np.zeros(num_steps+1)
T = np.zeros(num_steps+1)

Z[0] = 3.
H[0] = ((1.6*(10**6))-3.)
R[0] = 0.0
T[0] = 0.0



for i in range(num_steps):
  H[i+1] = H[i] + delta_t*h(i)
  Z[i+1] = Z[i] + delta_t*z(i)
  R[i+1] = R[i] + delta_t*r(i)
  T[i+1] = T[i] + delta_t
  
print (H[280])
print (Z[280])
print (R[280])
print (T[280])

plt.figure()
plt.step(T, H, '-b', where='post', label='Human Population ($H$) $\Delta t={:}$'.format(delta_t))
plt.step(T, Z, '-r', where='post', label='Zombie Population ($Z$) $\Delta t={:}$'.format(delta_t))
plt.step(T, R, '-g', where='post', label='Removed Population ($R$) $\Delta t={:}$'.format(delta_t))
plt.xlabel('Time ($days$)')
plt.ylabel('Population ($Q$) ')
plt.legend(loc='best')
plt.savefig('plot.png')

"""
plt.figure()
plt.step(T, Z, '-r', where='post', label='Euler $\Delta t={:}$'.format(delta_t))
plt.xlabel('Time ($t$)')
plt.ylabel('Zombie Population ($Z$)')
plt.legend(loc='best')
#plt.savefig('Zombie.png')

plt.figure()
plt.step(T, R, '-g', where='post', label='Euler $\Delta t={:}$'.format(delta_t))
plt.xlabel('Time ($t$)')
plt.ylabel('Removed Population ($R$)')
plt.legend(loc='best')
#plt.savefig('Removed.png')

"""