## The Fibonacci Sequencel
# A sequence of interger values in which the first two values are both 1 and each subsequent value is the sum
# of the two previous values.

# The first 11 terms of the sequence are: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# The Nth Fibonacci number can be computed by the recurrence relation (for n > 0):
# fib(N) = fib(N-1) + fib(N-2) if n > 1; fib(N) = N if n=1 or n=0

def fib(N):
    assert N >= 0, "Fibonacci NOT defined for N < 0."
    if N == 1 or N == 0:
        return 1
    return fib(N-1) + fib(N-2)

