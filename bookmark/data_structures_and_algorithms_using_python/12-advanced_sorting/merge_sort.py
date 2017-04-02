## Most sorting algorithm
# The merge sort algorithm use the divide and conquer strategy to sort the keys stored in a mutable sequence.
# The sequence of values is recursively divided into smaller and smaller subsequences until each value is contained 
# within its own sub-sequences.
# i.e. until left one item
# The subsequences are then merged BACK together to create a sorted sequence.

# Recusively splitting a list until each element is contained within its own list.

# There are two major steps in the merge sort algorithm:
# 1) dividing the list of values into smaller and smaller sublists
# 2) merging the sulists back together to create a sorted list.

# The use of recursion provides a simple solution to this problem.
# The list can subdivided by each recursive call and then merged back together as the recursion unwinds.

# basic recursion solution O(NlogN) time; O(N) space
def mergeSort(values):
    if not values:
        return values
    # base case - the list contains a single item.
    if len(values) == 1:
        return values
    middle = len(values) // 2
    # divide - narrow problem to smaller ones
    # split the list and perform the recursive steps
    left = mergeSort(values[:middle]) 
    right = mergeSort(values[middle:])
 
    # merge back
    return mergeOrdered(left, right)

def mergeOrdered(left, right):
    if not left:
        return right
    if not right:
        return left
    N, M = len(left), len(right)
    i, j = 0, 0
    result = []
    while i < N and j < M:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < N:
        result.append(left[i])
        i += 1
    while j < M:
        result.append(right[j])
        j += 1
    return result


# The above implementation has several disadvantages.
# 1) it relies on the use of the slice operation, which prevents us from using the function to sort 
#    an array of values since the array structure does not provide a slice operation.
# 2) The new physical sublists are created in each recursive call as the list is subdivided.
#    The slice operation can be time consuming since a new list has to be created and the contents of the slice
#    copied from the original list.
# 3) A new list is also created each time two sublists are merged during the unwinding of the recursion, 
#    adding yet more time to the overall process.
# 4) The sorted list is not contained within the same list originally passed to the function. 
#    i.e. it's not the in-place sorting.

## Improved implementation
# Instead of physically creating sublists when the list is split, we can use index markers to specify 
#   a subsequence of elements to create virtual sublists within the original physical list as was done with the
#   binary search.
# The use of virtual sublists eliminates the need to repeatedly create new physical arrays 
# or Python list structures during each recursive call.
# 
# This requires two index varaibles, first and last, for indicating the range of elements within the physical
# sublist that comprise the virtual sublist.
# 
# This implementation of the merge sort algorithm requires the use of a temporary array when merging the sorted virutal sublists.
#   Instead of repeatedly creating a new array and later deleting it each time sublists are merged, we can create a single array
#   and use it for every merge operation.
# Since this array is needed inside the mergeVirtual function, it has to either be declared as a global variable
#   or created and passed into the recursive function before the first call.

# in-place sorting, without return objects
def indexMergeSort(values, start, end, tmp):
    # base case
    if start == end:
        return
    # divide
    middle = (start + end) // 2
    indexMergeSort(values, start, middle, tmp)
    indexMergeSort(values, middle+1, end, tmp)
    # merge the two ordered subsequences
    mergeVirtual(values, start, middle+1, end+1, tmp)

# The tmp provides a temporary array needed for intermediate storage during the merging of the two subsequences.
# The array must be large enough to hold all of the elements from both subsequences.
# This temporary storage is needed since the resulting sorted sequence is not returned by the function
#   but instead is copied back to the original sequence structure.

def mergeVirtual(seq, left, right, end, tmp):
    # init two subsequence index variables.
    i, j = left, right
    #m = 0
    while i < right and j < end:
        if seq[i] < seq[j]:
            #tmp[m] = seq[i]
            tmp.append(seq[i])
            i += 1
        else:
            #tmp[m] = seq[j]
            tmp.append(seq[j])
            j += 1
        #m += 1
    # if the left subsequence contains more items append them to tmp
    while i < right:
        #tmp[m] = seq[i]
        tmp.append(seq[i])
        i += 1
        #m += 1
    # Or if right subsequence contains more, append them to tmp
    while j < end:
        #tmp[m] = seq[j]
        tmp.append(seq[j])
        j += 1
        #m += 1
    ## copy the sorted subseqence back into the original sequence structure.
    for i in xrange(end - left):
        seq[i+left] = tmp[i]
    print(seq)

if __name__ == "__main__":
    a = [9, 2, 3, 7, 5, 2, 4, 6, 1]
    print(mergeSort(a))
    indexMergeSort(a, 0, len(a)-1, [])
    print(a)          
         



