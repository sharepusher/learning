## The Linear Search 
# The simplest solution to the sequence search problem is the sequential or linear search algorithm.
# This technique iterates over the sequence, one item at a time, until the specific item is found or all items have been 
# examined. 
# In Python, a target item can be found in a sequence using the in operator.
# The use of the in operator makes our code simple and easy to read,
# BUT it hides the inner workings.
# Underneath, the in operator is implemented as a linear search.

## Linear Search on a un-sorted array

# @param: the list to search; the target to find
# @return: True or False
def linearSearch(values, target):
    if not values or not target:
        return False
    N = len(values)
    for i in xrange(N):
        if values[i] == target:
            return True
    return False

# To analyze the sequential search algorithm for the worst case, we must first determin what conditions 
# constitute the worst case.
# Remember, the worst case occurs when the algorithm performs the maximum number of steps.
# For a sequential search, that occurs when the target item is not in the sequence and the loop iterates over 
# the entire sequence.
# Assuming the sequence contains N items, the linear search has a worse case time of O(N). and O(1) space.


## Linear search on a sorted array.
# A linear search can also be performed on a sorted sequence, which 
# is a sequence containing values in a specific order.
# A linear search on a sorted sequence works in the same fashion as that for the unsorted sequence, with one exception.
# It's possible to terminate the search early when the value is not in the sequence instead of always having to perform
# a complete traversal.

def sortedLinearSearch(values, target):
    if not values or not target:
        return False
    N = len(values)
    for i in xrange(N):
        if values[i] > target:
            return False
        if values[i] == target:
            return True
    return False

# With the modification to the linear search alogrithm, we have produced a better version, BUT 
# the time complexity remains the same. The reason is that the worse case occurs when the value is not in the sequence
# and is larger than the last element.
# In this case, we must still traverse the entire sequence of N items.

## Finding the smallest value
# Instead of search for a specific value in an unsorted sequence, suppose we wanted to search for the smallest value, 
# which is equivalent to applying Python's min() function to the sequence.
# A linear search is performed as before, but this time we must keep track of the smallest value found for each iteration
# through the loop.

# To prime the loop, we assume the first value in the sequence is the smallest and start the comparisons at the second item.
# Since it's unsorted, the smallest value can occur anywhere in the sequence, we must always perform a complete 
# traversal, resulting in a worst case time O(N)

# @param: list of items
# @return: the smallest value
def findSmallest(values):
    if not values:
        return None
    smallest = values[0]
    N = len(values)
    for i in xrange(N):
        if values[i] < smallest:
            smallest = values[i]
    return smallest
    
