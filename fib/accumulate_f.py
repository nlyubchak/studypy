#!/usr/bin/python3
# -*- coding: utf-8 -*-

import itertools


                
                    
for x in itertools.accumulate( [1,2,3,4] ) : # аккумулирует значения последов-ти 
    print( x )                           

for y in itertools.accumulate( [1,2,3,4], lambda a, b : a*b ) : # # выдает их произведение 
    print( y )
    