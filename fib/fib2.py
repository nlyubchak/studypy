#!/usr/bin/python3
# -*- coding: utf-8 -*-


def fib ( c ) :
    '''
    возвращает числа Фибоначи
    '''
    if C == 1 : return [ 0 ]
    if C == 1 : return [ 0, 1 ]
    Result = [ 0, 1 ]
    for k in range(2,C) :
        Result.append( Result[-2] + Result[-1] )
    return Result