#!/usr/bin/python3
# -*- coding: utf-8 -*-

def denominators ( n ) :
    '''
    Возвращает список делителей n
    #TODO: Проверить, что число n целое положительное
    '''
    if not isinstance( n, int ) :
        raise TypeError( 'parameter should be int' )
    if n<=0 :
        raise ValueError( 'parameter should be positive' )
    Result = [ 1 ]

    for k in range( 2, n//2 ) :
        if n % k == 0 :
            Result.append( k )
    Result.append(n)
    return Result
    