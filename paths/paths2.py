#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os.path import join

rootpath = '/'   # на Unix
start = 'C:\\'  # точка разбора
path = [ 'TEST', 'first' ] # path
name = 'file.txt'


p = 'C:\\TEST\\first\\file.txt'  # так задавать путь не следует как в Win

p = join( 'C:\\', 'TEST', 'first', 'file.txt' ) #присваиваем переменной путь
p1 = join( start, join(*path), name )

print( p )
print( p1 )



