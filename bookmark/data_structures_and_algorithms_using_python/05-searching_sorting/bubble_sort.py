## Sorting
# Sorting is the process of arranging or ordering a collection of items such that each item and
# its successor satisfy a prescribed relationship.
# 
# The items can be simple values, such as integers and reals, or more complex types, such as student records
# or dictionary entries. In either case, the ordering of the items is based on the value of a sort key.
#
# The key is the value itself when sorting simple types or it can be a specific component or a combination of
# components when sorting complex types.
# 
## Bubble Sort
# A simple solution to the sorting problem is the bubble sort algorithm, which rearrange the values by iterating over
# the list multiple times, causing larger values to bubble to the top or end of the list.
# 
# Key of Bubble Sort, 1)  Larger item bubbles to the top or end.
# 2) During each pass, the first and the second positions are compared, if the first is larger than the second, 
# The two are swapped.

def bubbleSort(values):
    if not values:
        return values
    N = len(values)
    # traverse N-1 times, as the 
    for i in xrange(N-1):
        # N-1, as we need compare j and j+1
        # +i, as 
        # bubble the largest to the end.
        # by compare j and j+1
        for j in xrange(N-1-i):
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
    return values

# n^2 + n => resulting in a run time of O(N^2)
# Bubble sort is considered one of the most in-efficient sorting algorithms due to the total number of swaps required.
# The buble sort always performs N^2 iterations of the inner loop.
# What if the sequence is already in sorted order?
# 


if __name__ == "__main__":
    a = [9, 7, 3, 6, 9, 1, 5, 2, 4 ,1 , 1]
    print(bubbleSort(a))
             
