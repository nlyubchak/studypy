#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

def solve ( AA, BB, CC ) :
    D = BB*BB - 4*AA*CC
    if D >= 0 :
       X1 = ( -BB + math.sqrt(D) ) / ( 2.0 * AA )
       X2 = ( -BB - math.sqrt(D) ) / ( 2.0 * AA )
       return [X1, X2 ] 
    else:
       return []
      
A = float ( input( 'a: ' ) )
B = float ( input( 'b: ' ) )
C = float ( input( 'c: ' ) )

# TODO: Тут вызвать функцию

R = solve ( A, B, C )
print ( R )

print ( 'END' )

