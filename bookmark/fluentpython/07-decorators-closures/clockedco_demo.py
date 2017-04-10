import time
from clock_decorator import clock

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

# clock gets the factorial function as its func argument. 
# It then creates and returns the clocked function, which the python interpreter
# assigns to factorial behind the scenes. 
# In fact if you check the __name__ of factorial, factorial now actually
# holds a reference to the clocked function.
# From now on, each time factorial(n) is called, clocked(n) gets executed.
# In essence, clocked does the following:
# calls the original factorial, saving the result.
# This is the typicl behavior of a decorator:
# it replaces the decorated function with a new function that accepts the same arguments and
# returns whaterver the decorated function was supposed to return, 
# while also doing some extra processing.

 


if __name__ == "__main__":
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'calling factorial(6)')
    print('6!=', factorial(6))
    print(factorial.__name__)
