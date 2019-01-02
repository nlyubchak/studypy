#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

Num = re.compile( r'\d+' ) # от слеш - люб цифру, + - повторен один или много раз

X = input('X:')
M = Num.search( X )  # проверяет соотв рег выраж. М или сод-т выраж или будет none
if M :
    print( M.group(0) ) #список найденных частей вывести на экр.
    
    