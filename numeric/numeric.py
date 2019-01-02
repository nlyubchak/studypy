#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

A1 = np.array( [1, 2, 3, 4 ], dtype=np.int64 ) # create massive from Py. sequence


A2 = np.array( [ [  1, 2, 3, 4] ,  
               [10, 11, 12, 20 ] ], dtype=np.int64) # same with two-dimensional massive
X = A2[1,3]
Z = A2[1,:]  #: - ��� �������� 2-� ������
W = A2[:,3]

print( X )
print( Z )
print( W )

A3 = np.zeros( (3,4), dtype=np.complex128  ) # ������ ����������� �����

A4 = np.ones( (4,4), dtype=np.float64 )  # ��������� 1-����
A5 = np.identity( 5, dtype=np.float64 ) #1-��� �������
print ( A3 )
print ( A4 )
print ( A5 )
