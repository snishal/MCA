def sumUpTo(n):
    '''
    Objective : Compute Sum of Whole Numbers upto n.
    Input :
        n : Whole Number upto which sum is to be computed.
    Output : Returns Sum of Whole Numbers upto Input Number n.
    '''
    #Approach : sumUpTo(n) = n + sumUpTo(n-1)

    if (n == 1) or (n == 0):
        return n
    elif (n < 0):
        return 0
    
    return sumUpTo(n-1) + n
    

    
