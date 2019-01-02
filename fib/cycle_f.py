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
        for prev in select(n-1) :
            for s in Allowed :
                yield prev + s #берем послед-ть в 4 и добавляем еще один элемент
                
                    
for x in itertools.cycle( select (2) ) : # взяла последов-ть и гоняет ее по кругу 
    print( x )                           

