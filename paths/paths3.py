#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os.path import join
from os.path import normpath  #для нормализации пути
rootpath = '/'   # на Unix
drive = 'C:\\'  # точка разбора
path = [ '/' 'TEST', 'first' ] # path
name = 'file.txt'


p = normpath( join('C:', '/', 'TEST', 'first', 'file.txt' ) ) # имя устр-ва как прям косая черта, но только при модуле

p1 = normpath( join( drive, join(*path), name ) )

print( p )
print( p1 )



