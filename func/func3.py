#!/usr/bin/python3
# -*- coding: utf-8 -*-

# функция как элемент 1-го класса, можно присваивать перем и т.д.

def func1( a, b ) :
    print( 'func1:' )
    print( 'a -', a, ' b = ', b )

X = func1

func1(1,2)
X(1,2)

def func2( a ) :
    if a > 0 :
        return func1
    else :
        raise ValueError( 'Unknown value' )
print( func2( 2 ) )

Y = func2( 2 )(10,20)