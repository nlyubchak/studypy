#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os.path import join
from os.path import normpath  #для нормализации пути
from os.path import expanduser



drive = 'C:'  # 
start = '/'   # for Unix
path = [ 'start' 'TEST', 'first' ] # path
name = 'file.txt'


p = normpath( join('C:', '/', 'TEST', 'first', 'file.txt' ) ) # имя устр-ва как прям косая черта, но только при модуле

p1 = normpath( join( drive, join(*path), name ) )

p2 = normpath( expanduser( '~/.paths' ) ) # ~ - путь к папке с польз настроками
# точка обознач. - скрыт файл

print( p )
print( p1 )
print( p2 )



