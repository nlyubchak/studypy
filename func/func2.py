#!/usr/bin/python3
# -*- coding: utf-8 -*-

def func1( a, b ) :
    print( 'func1:' )
    print( 'a -', a, ' b = ', b )
# func1 = check_positive( func1 )

def func2( a ) :
    '''
    This is documentions
    '''
    if a > 0 :
        return func1
    else :
        def func3( x, y ) :
            print( 'func3:' )
            print('   x = ', x, ' y =', y, '  a=', a )
        return func3
        
func2( -1 )(10,20)
func2( 3 )(10,20)

# parameters
print( func2.__name__ )
# documents
print( func2.__doc__ )