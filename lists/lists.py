#!/usr/bin/python3
# -*- coding: utf-8 -*-

L = [ 1, 2.0, 'Вася Пупкин' ]
X = L[2]
L[2] = 'Пупкин Вася'

print ( L )
print ( X )

del L[1]

Z = L

Z.append( '!!!' )
Z.insert( 1, '???' )

print ( 'L =', L )

Z = [ 9, 8, 7 ]
print ( L )


X = L[1:3]
L[1:3] = [ 1, 2, 3, 4, 5 ]
print ( L )
print ( X )
Y = L[4:]
Z = L[:2]
W = L[-2:]
print ( Z )
print ( W )