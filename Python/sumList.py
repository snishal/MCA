def sumList(list):
    '''
    objective: computer sum of elements of a list.
    input:
        list: a list whose sum is to be computed
    output: sum of the elements of a list
    '''
    #Approach: sumList(list) = firstElementOfList + sumList(list with remaining elements)

    if list == []:
        return 0
    return list[0] + sumList(list[1:])
