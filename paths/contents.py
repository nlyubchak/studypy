#!/usr/bin/python3
# -*- coding: utf-8 -*-

# в данном случае работаем с менеджером контента через with
with open( 'test.txt', 'wt', encoding='utf-8' ) as TRG : #команда with  знает, что нужно сделать с файлом, т.е закр например в конце
                               
    print( 'Вася Пупкин', file=TRG )
    print( 'Пупкин Вася ', file=TRG )
    print( 'Москва'     , file=TRG )
