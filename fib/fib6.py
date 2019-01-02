#!/usr/bin/python3
# -*- coding: utf-8 -*-

#!/usr/bin/python3
# -*- coding: utf-8 -*-

   
def factorize( n ) :
    '''
    написать генератор функцию - возвращает послед-ть, а не список
    '''
    if n < 1 :
        raise ValueError( 'Inacceptable value')
    for k in range(2,n) :
        if n <= 1 : break
        while n % k == 0 : # если n делится на k без остатка
            yield k    # выдаем на выход
            n //= k  # instead n = n // k
            
    else :
        yield(n) 
        
for n in factorize(100) :
    print( n )
    