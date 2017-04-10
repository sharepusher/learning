#
# Summarize
#

# The first crucial fact: they have the power to replace the decorated function with a different one.
# The second crucial fact is that they are executed immediately when a module is loaded.


def deco(func):
    def inner():
        print("running the decorator")
        func()
    return inner

@deco
def target():
    print("running original target")

target()
# Inspection reveals that target is now a REFERENCE to inner.
print(target)

# Strictly speaking, decorators are just syntactic sugar.
# meta-programming: changing program behavior at runtime.

# Function decorators let us 'mark' funcitons in the source code to enhance their behavior in some way.
# This is powerful stuff, but mastering it requires understanding closures.

# One of the newest revered keywords in Python is nonlocal, introduced in Python3.0.
# You can have a profitable life as a Python programmer without ever using it if you adhere to 
# a strict regimen of class-centered object orientation.
# However, if you want to implement your own function decorators, you must know closures inside out, and then the need for nonlocal
# becomes obvious.

# Aside from their application in decorators, colsures are also essential for effective asyn-chronous programming with callbacks,
# and for coding in a functional style whenever it makes sense.

# The end goal of this chapter is to explain exactly how function decorators work, 
# from the simplest registration decorators to the rather more complicated parameterized ones.

# How python evaluates decorator syntax
# How python decides whether a variable is local
# why colsures exist and how they work
# what problem is solved by nonlocal

# with this grounding, we can tackle further decorator topics:
# Implementing a well-behaved decorator
# Interesting decorators in the standard library
# Implementing a parameterized decorator

# we start with a very basic introduction to decorators, and then proceed with the rest of 
# the items listed here.

# decorators 101
# A decorator is a callable that takes another function as argument(the decorated function).
# The decorator may perform some processing with the decorated function, 
# and returns it or replaces it with another function or callable object.

# In other words, assuming an existing decorator named decorate, this code:
# @decorate
# def target():
#     print("running target()")
# Has the same effect as writing this:
# def target():
#    print("running target()")
# target = decorate(target)

# the end result is the same: at the end of either of these snippets, the target name does not necessarily to the original
# target function, but to whatever function is reuturned by decorate(target)

# To confirm that the decorated function is replaced, see the console session in examples
# a decorator ususally replaces a function with a different one
# def deco(func):
#      def inner():
#           print("running inner()")
#      return inner
# @deco
# def target():
#     print("running target()")
# 
# target()
# running inner()
# target
# function deco.<locals>.inner at 0x10063b598














