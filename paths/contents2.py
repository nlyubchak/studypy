#!/usr/bin/python3
# -*- coding: utf-8 -*-

TRG = open( 'test.txt', 'wt', encoding='utf-8' )

try :                                 # это чтобы корректно закрыть файл
    print( 'Вася Пупкин', file=TRG )
    print( 'Пупкин Вася ', file=TRG )
    print( 'Москва'     , file=TRG )
finally:
    TRG.close()
    
