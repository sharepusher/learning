## Insertion Sort
# pivot sort?
# Another commonly studied sorting algorithm is the insertion sort.

# The insertion sort maintains a collection of SORTED items,
# and a collection of items to be sorted.

# The insertion sort is an example of a sorting algorithm in which the best and worst cases are different.

def insertionSort(values):
    if not values:
        return values
    N = len(values)
    # by default, the first one is a sorted list!!!!!
    # so it's still N-1 passes
    for i in xrange(1, N):
        # we will compare i with previous ones in reverse order
        # key: how to reverse
        tindex = i
        for j in xrange(i-1, -1, -1):
            if values[j] <= values[tindex]:
                break
            values[j], values[tindex] = values[tindex], values[j]
            tindex = j
    return values

if __name__ == "__main__":
    print(insertionSort([5, 1, 3, 2, 9, 7, 6]))
