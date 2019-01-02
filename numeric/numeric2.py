
def pol_value( pol, x) :
    Result = 0
    for a in pol :
        Result = Result * x + a
    return Result
    
def roots ( pol ) :
    A0 = pol[-1]
    if A0 == 0 : 
        # FIXME: Не можем получить все целые корни,
        # не вычисляя их кратности
        return [0]
    Result = []
    for p in num.denominators ( A0 ) :
        if pol_value( pol, p )  == 0 :
            Result.append( p )
        if pol_value( pol, -p )  == 0 :
            Result.append( -p )
            
    return Result
          
    
    