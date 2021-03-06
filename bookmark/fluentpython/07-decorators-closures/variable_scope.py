# function reading a local and a global variable

def f3(a):
    global b
    print(a)
    print(b)
    b = 9


b = 6

def f2(a):
    print(a)
    # when python compile the body of the function, it decides that b is a 
    # local variable because it is assigned within the function.
    # The generated bytecode reflects this decision and will try to fetch b from the local 
    # environment. But when trying to fetch the value of local variable it discovers that 
    # b is unbound.
    
    # This is not a bug, but a design choice: Python DOES NOT require you to declare variables
    # but assumes that a variable assigned in the body of a function is local.
    
    # if we want the interpreter to treat b as a global variable in split of the assigment within the function
    # we use the global declaration.
    print(b)
   
    b = 9
#f1(3)

f2(3)


