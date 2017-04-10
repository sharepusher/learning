## Quick Sort vs Merge Sort
# Both of them use the divide and conquer strategy.
# The key of quick sort is "Pivot", and "partition".
# The key of merge sort is the "midpoint" and "merge".

# The quick sort partitions the sequence by dividing it into two segments based on a selected pivot key.
# In addition, the quick sort can be implemented to work with virutal subsequences without the need 
# for temporary storage.

# The quick sort is a simple recursive algorithm that can be used to sort keys stored in either an array or list.

# The FIRST key is selected as the pivot.

# A simple implementation using the slice operation can be devised for the quick sort algorithm as was done 
# with the merge sort but it would require the use of temporary storage.

# An efficient solution can be deisigned to work with virtual subsequences or segments that does not 
# require temporary storage.
# However, it is not as easily implemented since the partitioning must be done using the same sequence
# structure.

## Efficiency Analysis
# The quick sort algorithm has an average or expected time of O(nlogn)
# BUT runs in O(N^2) in the worst case.
# Even though quick sort is quadratic in the worst case, it does approach the average
# case in many instances and has the advantage of not requiring additonal temporary
# storage as in the case with the merge sort.
# The quick sort is the commonly used algorithm to implement sorting in language libraries.
# Earlier version of Python used quick sort to implement the sort() method of the list structure.
# In a current version, a hybrid algorithm that combines the insertion and merge sort
# algorithm is used instead.


## Implementation - in place sort
def quickSort(seq):
    N  = len(seq)
    recQuickSort(seq, 0, N-1)

def recQuickSort(seq, start, end):
    # base case
    # start > end to handle the seq empty case.
    if start >= end:
        return    
    pivot = seq[start]
    # divide
    # find the position index
    pos = partitionSeq(seq, start, end)
    # after partition, the pivot index will be changed.
    recQuickSort(seq, start, pos-1)
    # in other words, the pivot is settle down, no need to put it into the rec sort seq indexes.
    recQuickSort(seq, pos+1, end)
    

# O(N)
# compare with pivot, like the insertion sort?
# 
def partitionSeq(seq, start, end):
    pivot = seq[start]
    left, right = start + 1, end
    while left <= right:
        while left <= right and seq[left] < pivot:
            left += 1
        while left <= right and seq[right] >= pivot:
            right -= 1
        # now the left > pivot, and the right < pivot, exchange them
        if left < right:
            seq[left], seq[right] = seq[right], seq[left]
            
        # put the pivot the proper place
        # now, left should be the first one that greater than 
    if start != right:
        seq[start], seq[right] = seq[right], seq[start]
    # Now, right is the pivot index
    return right

            
    
if __name__ == "__main__":
    a = [9, 7, 6, 2, 3, 7, 7, 7]
    b = [2,2,2,2]
    print("Before quick sort:", a)
    quickSort(a)
    quickSort(b)
    print("After quick sort:", a)
    print("After quick sort:", b)

## How fast can we sort?
# The comparison sort algorithms achieve their goal by comparing the individual sort keys
# to other keys in the list.
# We have reviewed five sorting algorithms. The first three, bubble, selection, and insertion, have a 
# worse case time of O(N^2) while the merge sort has a worst case time of O(NlogN).
# The quick sort, the more commonly used algorithm in language libraries, is O(N^2) in the worst case 
# but it has an expected or average time of O(NlogN).
# For a comparison sort, the answer is no.
# It can be shown, with the use of a decision tree and examining the permutations of all possible
# comparisons among the sort keys, that the worst case time for a comparison sort can be no better than O(logN).
# A distribution sort algorithm that works in linear time.
# Distrbution sort algorithms use techniques other than comparsions among the keys themselves to sort 
# the sequence of keys.
# While there distribution algorithms are fast, they are not general purpose sorting algorithms.
# In other words, they cannot be applied to just any sequence of keys.
# Typically, these algorithms are used when the keys have certain characteristics and for specific types of 
# applications.
 


