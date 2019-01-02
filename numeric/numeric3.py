#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

A1 = np.array( [1, 2, 3, 4 ], dtype=np.int64 ) # create massive from Py. sequence


A2 = np.array( [ [  1, 2, 3, 4] ,  
               [10, 11, 12, 20 ] ], dtype=np.int64) # same with two-dimensional massive
X = A2[1,3]
Z = A2[1,:]  #: - все значения 2-й строки
W = A2[:,3]

print( X )
print( Z )
print( W )

A3 = np.zeros( (3,4), dtype=np.complex128  ) # массив комплексных нулей

A4 = np.ones( (4,4), dtype=np.float64 )  # заполнена 1-цами
A5 = np.identity( 5, dtype=np.float64 ) #1-ная матрица
print ( A3 )
print ( A4 )
print ( A5 )

E = A+B # почленное сложение
D = A*B # почленное умножение

C = np.dot(A,B) #произведение матриц

print ( E )
print ( D )
print ( C )

