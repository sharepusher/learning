## Sorted Lists
# Sorting  algorithms can be used to create a sorted sequence, but they are typically applied to an unsorted sequence
# in which all of the values are known and the collections remains STATIC. 
# In other words, No new items will be added to the sequence NOR will any be removed.
# Instead, the sorted list can be maintained as the collection changes by inserting the new item into its proper position
# without having to re-sort the entire list.
# Note that while the sorting algorithm from the previous section all require O(N^2) time in the worst case, there are 
# more efficient sorting that only require O(NlogN) time.

## Maintaining a Sorted List
# To maintain a sorted list in real time, new items must be inserted into their proper position.
# The new items cannot simply be appended at the end of the list as they may be out of order.
# Instead, we must locate the proper position whithin the list and use the insert() method
# to insert it into the indicated position.
# 
# i.e. The key to maintaining sorted list, is to locate the postion of target.
# 

# find the first postion that greater than the target, find the last position that smaller than the target 
# @return: the index of target or -1
def findSortedPosition(values, target):
    if not values or target is None:
        return -1
    N = len(values)
    start, end = 0, N-1
    while start + 1 < end:
        middle = (start+end) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            start = middle
        else:
            end = middle
    if values[end] <= target:
        return end
    if values[start] <= target:
        return start

# two pointers - O(N) time, O(N)space.
## Merging sorted lists
def mergeSortedLists(A, B):
    if not A:
        return B
    if not B:
        return A
    N, M = len(A), len(B)
    i, j = 0, 0
    result = []
    # either of them finished, then we should stop
    while i < N and j < M:
        if A[i] <= B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1
    # now one of them finished
    if i < N:
        result.append(A[i:])
    elif j < M:
        result.append(B[j:])
    return result
                
         
