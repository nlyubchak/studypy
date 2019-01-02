#!/usr/bin/python3
# -*- coding: utf-8 -*-

def fib ( C ) :
    if C < 0:
        raise ValueError( 'Negative sequence lenth' )
    if C > 0 :
        yield 0 
        if C > 1 :
            yield 1
            a, b = 0, 1
            for k in range( 2, C ) :
                a, b = b, a+b #запомнили предыдущ члены
                yield b
                    
for n in fib(10) :
    print( n )
    