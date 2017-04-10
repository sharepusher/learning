## The Binary Search
# This is an example of a divde and conquer strategy
# which entails dividing a large problem into smaller parts and conquering the smaller part.

# works on SORTED sequence.
# The alogrithm starts by examining the middle item of the sorted sequence, resulting in one of 
# the three possible conditions: the middle item is the target value, the target value 
# is less than the middle item, or the target is larger than the middle item.
# Since the sequence is ordered, we can eliminate half the values in the list when the target value is not found
# at the middle position.

# @params: list of values, the target
# @return: True or False
def binarySearch(values, target):
    if not values or target is None:
        return False
    N = len(values)
    start, end = 0, N-1
    while start + 1 < end:
        middle = (start+end) //2
        if values[middle] == target:
            return True
        if values[middle] < target:
            start = middle
        else:
            end = middle
    # now only start, and end 
    if values[start] == target:
        return True
    if values[end] == target:
        return True
    return False

# The worse case occurs when the target value is not in the sequence, the same as the linear search.
# The difference with the binary search is that to every item in the sequence has to be examined before determining 
# the target is not in the sequence, even in the worst case.
# Since the sequence is sorted, each iteration of the loop can eliminate from consideration half of the remaining values.
# When the input size is repeatedly reduced by half during each iteration of a loop, there will be logN iterations in the 
# worse case. Thus, the binary search algorithm has a worst case time-complexity of O(logN).

