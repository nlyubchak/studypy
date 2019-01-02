#!/usr/bin/python3
# -*- coding: utf-8 -*-

def fib (  ) :
    '''
    generator-function
    '''
        yield 0 
        yield 1
        a, b = 0, 1
        while True : # forever
            a, b = b, a+b #запомнили предыдущ члены
            yield b
                    
for n in fib() :
    print( n )
        