## Selection Sort
# Improves on the bubble sort and works in a fashion similar to what a human may use to sort.
# 
# Instead swapping the j and j+1 that was done with the bubble sort, the selection sort, will find the smallest one by one
# by scan all the list, just like the find minimum in linear list

# compared with bubble sort, which is a in-place replacement, and return the original list
# while, selection sort needs a list to collect the minimal one by one
# therefore, O(N)-space is needed.
# How to make the selection sort inplace?
# !!! Exchange the items to front

def selectionSort2(values):
    if not values:
        return values
    N = len(values)
    for i in xrange(N-1):
        #minimal = values[i]
        for j in xrange(i+1, N):
            if values[j] < minimal:
                vlaues[i], values[j] = values[j], values[i]
    return values    
#
# The selection sort, which makes n-1 passes over the array to reposition N-1 values, is also O(N^2)
# The difference between the selection and bubble sort is that 
# the selection sort reduces the number of swaps required to sort the list to O(N)
#
def selectionSort3(values):
    if not values:
        return values
    N = len(values)
    for i in xrange(N-1):
        minIndex = i
        for j in xrange(i+1, N):
            if values[j] < values[i]:
                minIndex = j
        if minIndex != i:
            values[i], values[minIndex] = values[minIndex], values[i]
    return values

# @params: original list
# @return: sorted list
def selectionSort(values):
    if not vlaues:
        return values
    newvalues = []
    # find minimal one by one
    N = len(values)
    for i in xrange(N):
        minimal = values[0]
        for j in xrange(len(values))
            if values[j] < minimal:
                minimal = values[j]
        newvalues.append(minimal)
        values.remove(minimal)
    return newvalues
     
    
