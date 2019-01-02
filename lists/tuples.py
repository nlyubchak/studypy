#!/usr/bin/python3
# -*- coding: utf-8 -*-

C = ( 1967, 'Вася Пупкин', 'Москва', )
# W = ( 1678, 'Петр Первый', ( 'Москва', 'Санк-Петербург' ) )

( year, name, city ) = C

a = 5

( a, b ) = ( a+1, a )



print( C )
print( year, name, city ) 

D = {
     'year': 1967,
     'name': 'Вася Пупкин',
     'city': 'Москва',
}

X = D['year']
D['year'] = 1247

print( '---' )
for k in C :
    print( k ) 
print( '---' )
for key in D :
    print(key )
print( '---' )   
for ( key, value ) in D.items () :
    print( key, '=>', value )