#!/usr/bin/python3
# -*- coding: utf-8 -*-

import itertools


Allowed = [ 'a', 'b', 'c' ] #список допустимых припереборе элементов
def select( n ) :
    '''
    generator passwords выдает элементы по одному
    '''
    if n == 0 :
        yield ''
    else :
        for prev, s in itertools.product( select(n-1), Allowed ) : # product работает с конечн послед
                 yield prev + s #
                

                    
for x in select( 5 ) : # 
    print( x )                           
