#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os.path import join
from os.path import normpath  #для нормализации пути
from os.path import expanduser
from os.path import expandvars
from os.path import split
import os
drive = 'C:'  # 
start = '/'   # for Unix
path = [ 'start' 'TEST', 'first' ] # path
name = 'file.txt'


p = normpath( join('C:', '/', 'TEST', 'first', 'file.txt' ) ) # имя устр-ва как прям косая черта, но только при модуле

p1 = normpath( join( drive, join(*path), name ) )

p2 = normpath( expanduser( '~/.paths' ) ) # ~ - путь к папке с польз настроками

p3 = normpath( expandvars( join('%PATH%/test' ) ) )

p4 = normpath( 'vasya/petrov/../pupkin/file.txt')

print( p )
print( p1 )
print( p2 )
print( p3 )
print( split(p1) ) # split - cut for two piece path and file name

Croot = normpath( join( 'C:', '/' ) ) 

for path, dirs, files in os.walk( Croot ) : # walk - show files structures
    if 'Program Files' in dirs :
        dirs.remove( 'Program Files' ) #exclude this directory
    if 'Program Files (x86)' in dirs :
        dirs.remove( 'Program Files (x86)' )
    if 'Program Data' in dirs :
        dirs.remove( 'Program Data' )
    for f in files :
        try :
            print( join(path, f ) )
        except UnicodeEncodeError :
            print( '???' )
            pass # ничего не делает
        



