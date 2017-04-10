## Recursive Functions
# A function or method can call any other function( or method), including itself. 
# A function that calls itself is Known as a RECURSIVE FUNCTION.
# The result is a virtual loop or repetition used in a fashion similar to a while loop.

## Local Variables
# Like any other function, each call to a recursive function creates new instances of all local
# reference variables used within that function.
# Chaning the contents of a local reference variable does not affect the contents of other instances of that 
# variable.

## Example
# Consider the simple problem of printing the integer values from 1 to n in reverse order

# recursion
# print num in reverse order
def printInter3(n):
    if n >= 1:
        print(n)
        printInter3(n-1)
    print("Finished the recursive function call with reversed numbers")
# print num in increasing order
def printInter4(n):
    # The base case is the terminating case n==0
    # and represents the smallest subdivison of the problem.
    # The recursive case is performed for all values of n > 0
    if n > 0:
        printInter4(n-1)
        print(n)

# non-recursion
def printInter1(n):
    while n >= 1:
        print(n)
        n -= 1
    print("Finished the print integer.")
def printInter2(n):
    # be careful the xrange reverse order
    # is xrange(N, 0, -1) BUT NOT 0,N,-1
    for i in xrange(n,0,-1):
        print(i)
    print("Finished the print interger2.")

if __name__ == "__main__":
    printInter1(5)
    printInter2(9)
    printInter3(3)
    printInter4(6)
