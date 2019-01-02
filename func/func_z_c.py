#!/usr/bin/python3
# -*- coding: utf-8 -*-


def select_min( words, func ) :
    Result = func(words[0]) #взяли нулевое слово, вырезали 3 первых буквы
    for R in words :
        R = func(R)
        if Result > R :
            Result = R 
    return Result

# def f3( word ) :
#    return word[:3]

select_min( words, lambda word : word[:3] ) #вместо 29-30


# замыкание - closure

def compare( x, y ) :
    return x > y

compare(x,0)
compare(x,1)

over0 = lambda x : compare( x, 0 ) #замыкание

# каррирование- передача 2-х параметров, когда есть только 1

comp = lambda x : lambda y : compare(x,y) #берем ф-цию c фиксир парам. x и вызывыв. ее с парам y
 # или вот так
# def comp( x ) :
 #   def comp1( y ) :
#        return compare( x, y )
#    return comp1

comp(x)(y)

