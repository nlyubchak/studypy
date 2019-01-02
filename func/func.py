#!/usr/bin/python3
# -*- coding: utf-8 -*-

def check_positive( func ) :
    def checked( a, b ) :
        if a <= 0 :
            raise ValueError( 'value must be positive' )
        return func( a, b )
    return checked
        
def func1( a, b ) :
    print( 'func1:' )
    print( 'a -', a, ' b = ', b )
# func1 = check_positive( func1 )

@check_positive  #14str = 16 str
def func4(a, b ) :
    print( 'func4' )

func4( 1, 2 )
func4( 1, 2 )








        
    
