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


