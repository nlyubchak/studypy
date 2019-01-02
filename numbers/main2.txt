#!/usr/bin/python3
# -*- coding: utf-8 -*-


import num

try :
    N = eval( input(': ') )
    L = num.denominators( N )
    print( L )
except ValueError :
    print( 'Вводите правильное значение' )
except :
    print( 'Что-то случилось' )
    raise
else :
    print( 'OK' )
finally : 
    print( 'END' )
    


      
print( '---------------')

for x in range( 100, 105 ) :
    print( x, '=>', num.factorize(x) )

print( '---------------')

for x in range( 100, 105 ) :
    print( x, '=>', num.denominators(x) )
    
print( '---------------')   

print( num.NOD( 122, 12 ) )

print( '---------------')   


    
