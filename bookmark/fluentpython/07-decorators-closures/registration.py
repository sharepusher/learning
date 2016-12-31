#
# Summary
#

# The decorator function may be NOT defined in the same module as the decorated functions.
# A real decorator is usually defined in one module and applied to functions in other modules.

# In practice, most decorators define an inner function and return it but NOT the same 
# function passed as argument.

# The decorator are excuted as soon as the module is imported(at import time);
# the decorated functions only run when they are explicitly invoked (at runtime).


registry = []

def register(func):
    print("running register(%s)" % func) 
    registry.append(func)
    return func

@register
def f1():
    print("running f1()")

@register
def f2():
    print("running f2()")

def f3():
    print("running f3()")

def main():
    print("running main()")
    print("registry ->", registry)
    f1()
    f2()
    f3()

if __name__ == "__main__":
    main()

#
# OUTPUT
#

#running register(<function f1 at 0x107f3e0c8>)
#running register(<function f2 at 0x107f3e6e0>)
#running main()
#('registry ->', [<function f1 at 0x107f3e0c8>, <function f2 at 0x107f3e6e0>])
#running f1()
#running f2()
#running f3()

#>>> import registration
#running register(<function f1 at 0x106ab60c8>)
#running register(<function f2 at 0x106ab66e0>)


