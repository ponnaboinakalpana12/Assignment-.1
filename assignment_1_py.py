# -*- coding: utf-8 -*-
"""ASSIGNMENT 1.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iywd5yr0jDa4DmoiCJq3j-gci0vbFXkI
"""

83# -*- coding: utf-8 -*-
"""ASGNMNT1.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1owmZtvVEpf99v89cYubO7nPqel_wKkVy
"""
 
# -*- coding: utf-8 -*-
"""ASSIGNMENT1.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1vBNusvh2DYwvn5tTXWedduY4IItE9SEJ
"""
 
# -*- coding: utf-8 -*-
"""coeffs.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1BENeKzBauyOjSYqXOpynAcVoj0eB845R
"""
 
import numpy as np
 
 
def dir_vec(A,B):
  return B-A
 
def norm_vec(A,B):
  return np.matmul(omat, dir_vec(A,B))
 
#Generate line points
#def line_gen(A,B):
#  len =10
#  dim = A.shape[0]
#  x_AB = np.zeros((dim,len))
#  lam_1 = np.linspace(0,1,len)
#  for i in range(len):
#    temp1 = A + lam_1[i]*(B-A)
#    x_AB[:,i]= temp1.T
#  return x_AB
 
#Generate line intercepts
def line_icepts(n,c):
  e1 = np.array([1,0]) 
  e2 = np.array([0,1]) 
  A = c*e1/(n@e1)
  B = c*e2/(n@e2)
  return A,B
 
#Generate line points
def line_dir_pt(m,A,k1,k2):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB
#Generate line points
 
def line_norm_eq(n,c,k):
  len =10
  dim = n.shape[0]
  m = omat@n
  m = m/np.linalg.norm(m)
#  x_AB = np.zeros((dim,2*len))
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k[0],k[1],len)
#  print(lam_1)
#  lam_2 = np.linspace(0,k2,len)
  if c==0:
    for i in range(len):
      temp1 = lam_1[i]*m
      x_AB[:,i]= temp1.T
  else:
    A,B = line_icepts(n,c)
    for i in range(len):
      temp1 = A + lam_1[i]*m
      x_AB[:,i]= temp1.T
#    temp2 = B + lam_2[i]*m
#    x_AB[:,i+len]= temp2.T
  return x_AB
 
#def line_dir_pt(m,A, dim):
#  len = 10
#  dim = A.shape[0]
#  x_AB = np.zeros((dim,len))
#  lam_1 = np.linspace(0,10,len)
#  for i in range(len):
#    temp1 = A + lam_1[i]*m
#    x_AB[:,i]= temp1.T
#  return x_AB
 
 
#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
 
#Foot of the Altitude
def alt_foot(A,B,C):
  m = B-C
  n = np.matmul(omat,m) 
  N=np.vstack((m,n))
  p = np.zeros(2)
  p[0] = m@A 
  p[1] = n@B
  #Intersection
  P=np.linalg.inv(N.T)@p
  return P
 
#Intersection of two lines
def line_intersect(n1,c1,n2,c2):
  N=np.vstack((n1,n2))
  p = np.array([c1,c2]) 
  #Intersection
  P=np.linalg.inv(N)@p
#  P=np.linalg.inv(N.T)@p
  return P
 
 
 
# -*- coding: utf-8 -*-
"""ASSIGNMENT1.ipynb
Automatically generated by Colaboratory.
Original file is located at
https://colab.research.google.com/drive/1vBNusvh2DYwvn5tTXWedduY4IItE9SEJ#scrollTo=bkHCUx24AeJ7&line=5&uniqifier=1
"""
 
#Code by P. Kalpana
#May 19, 2021
#Drawing a triangle DEF
 
import numpy as np
import matplotlib.pyplot as plt
 
 
 
#Sides
DE = 5
DF= 3
 
 
#Calculating third side 
EF=((DE*DE)+(DF*DF))
 
#Triangle vertices
D= np.array([0,0]) 
E= np.array([0,DE]) 
F = np.array([DF,0]) 
 
 
#Generating all lines
x_DE = line_gen(D,E)
x_DF = line_gen(D,F) 
x_EF = line_gen(E,F)
 
#Plotting all lines
plt.plot(x_DE[0,:],x_DE[1,:],label='$DE$')
plt.plot(x_DF[0,:],x_DF[1,:],label='$DF$')
plt.plot(x_EF[0,:],x_EF[1,:],label='$EF$')
 
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 + 0.1), E[1] * (1 - 0.1) , 'E')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 - 0.2), D[1] * (1) , 'D')
plt.plot(F[0], F[1], 'o')
plt.text(F[0] * (1 + 0.03), F[1] * (1 - 0.1) , 'F')
 
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor