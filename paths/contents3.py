#!/usr/bin/python3
# -*- coding: utf-8 -*-

# в данном случае работаем с менеджером контента через with
with open( 'test.txt', 'wt', encoding='utf-8' ) as TRG : #команда with  знает, что нужно сделать с файлом, т.е закр например в конце
                               
    print( 'Вася Пупкин', file=TRG )
    print( 'Пупкин Вася ', file=TRG )
    print( 'Москва'     , file=TRG )
with open( 'test.txt', 'rt', encoding='utf-8' ) as SRC :
    for line in SRC :
        if line[-1] == '\n' : line = line[:-1] #выкидываем посл символ
        print( line )
      