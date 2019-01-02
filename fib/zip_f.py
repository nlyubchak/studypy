#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
                
                    
for x in zip( range(0,100), select (5) ) : # первый элемент взят из range второй из select, 
    print( x )                             # но закончивает там где кончилась самая коротк послед.
