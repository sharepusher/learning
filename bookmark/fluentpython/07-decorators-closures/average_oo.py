#
# Summary
#

# A closure is a function that retains the bindings of the free variables that exist when the function is defined.
# So that they can be used later when the function is invoked and the defining scope is no longer available.

# NOTE that the ONLY situation in which a functiion may need to deal with external variables that are nonglobal 
# is when it is nested in another function.



class Average():
    """Calculate a running average.
    """
    def __init__(self):
        self.series = []
    
    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)


# A higher-order function to calculate a running average
def make_average():
    series = []
    def average(new_value):
        # The closure for average extends the scope of function to include the binding for the free variable series
        # series is a free variable.
        # This is a technical term meaning a variable that is not bound in the local scope.
        series.append(new_value)
        total = sum(series)
        return total//len(series)
    return average

if __name__ == "__main__":
    avg = Average()
    print(type(avg))
    print(avg)
    print(avg(10))
    print(avg(11))
    print(avg(12))
  
    new_avg = make_average()
    print(new_avg)
    print(type(new_avg))
    print(new_avg(10))
    print(new_avg(11))
    print(new_avg(12))

    # Inspecting the function created by make_average
    print(new_avg.__code__.co_varnames)
    print(new_avg.__code__.co_freevars)  
    # The binding for series is kept in the __closure__attribute of the returned function average.
    # Each item in new_avg.__closure__ corresponds to a name in new_avg.__code__.co_freevars
    # These items are cells, and they have an attribute called cell_contents where the actual value can be found.
    print(new_avg.__closure__)
    print(new_avg.__closure__[0].cell_contents)

