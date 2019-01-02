#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Проверка 1-го числа, что оно положительное
def check_type( func ) :
    def checked( *args ) :
        if args[0] <= 0 :
            raise ValueError( 'value must be positive' )
        return func( *args )
    return checked
        

@check_type
def func4(a, b, c ) :
    print( 'func4' )
# 
# декоратор взамен этого- func4 = check_type(int)(func4)

func4( 1, 2, -6 )
func4( 1, 2, -3 )

    











        
    
