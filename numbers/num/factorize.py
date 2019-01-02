#!/usr/bin/python3
# -*- coding: utf-8 -*-

def factorize( n ) :
    '''
    Дано целое число. Возвращает список его простых делителей
    #TODO: Проверить, что это целое полож. число
    '''
    Result = []
    for k in range(2,n) :
        if n <= 1 : break
        while n % k == 0 :
            Result.append( k )
            n = n // k
            
    else :
        Result.append(n)
    return Result
    