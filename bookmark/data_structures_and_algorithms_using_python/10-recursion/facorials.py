## Factorials
# The factorial of a positive integer n can be used to calculate the number of permutations of n elements.
# The function is defined as:
# n! = n * (n-1) * (n-2) * ... * 1
# With the specail case 0! = 1.

# The problem can be solved easily using an iterative implementation that loops through the individual values[1...n]
# and computes a product of those values.
# BUT it can also be solved with a recursive solution and provides a simple example of recursion.
# Consider the facorial function on different integer values:
# 0! = 1; 1 ! = 1; 
# 2! = 2 * 1 = 2 * 1! = 2*(2-1)!;
# 3! = 3 * 2 * 1 = 3 * 2! = 3 * (3-1)!
# 4! = 4 * 3 * 2 * 1 = 4 * 3! = 4 * (4-1)!
# After careful inspection of these equations, it becomes obvious each of the successive equations,
# for n > 1, can be rewritten in terms of the previous equation.
# Since the function is defined in terms of itself and contains a base case,
# a recursive definition can be produced for the factorial function as shown:
# n! = 1 if n=0; n!=n*(n-1) if n > 0 

# compute N!
# recursion
def factorials2(N):
    # corner case
    assert N >= 0, "Factorial not defined for negative values."
    # base case
    if N <= 1:
        return 1
    # recursive case 
    return N * factorials2(N-1)

# non-recursion
def factorials1(N):
    if N <= 1:
        return 1
    result = 1
    for i in xrange(N, 0, -1):
        print(i)
        result *= i
    print("Finished the factorials counting: %d" % result) 

if __name__ == "__main__":
    factorials1(5)
    print("recursion result of 5!: %d " % (factorials2(5)))
