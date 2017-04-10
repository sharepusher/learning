# Implementation of the Set ADT container using a Python list.

# KEY words:
# Unique valuess, no particular ordering.

# What is Set?
# A set stores UNIQUE values and represents the same structure found in mathematics.

# When to use?
# It is commonly used when you need to store a collection of unique values without regard to how they are stored
# or when you need to perform various mathematical set operations on collections.

#Set ADT
# Set(): Creates a new set initialized to the empty set.
# length(): Returns the number of elements in the set, also known as the cardinality. Accessed using the len() func.
# contains(element): Determins if the given value is an element of the set and returns the appropriate boolean value.
#     Access using the in operator.
# add(element): Modifies the set by adding the given value or element to the set if the element is not already a member.
#     If the element is not unique, no action is taken and the operation is skipped.
# remove(element): Removes the given value from the set if the value is contained in the set and raises an exception otherwise.
# equals(setB): Determins if the set is a subset of another set and returns a boolean value.
#     For set A to be a subset of B, all elements in A must also be elements in B.
# union(setB): Creates and returns a new set that is the union of this set and setB. 
#     The new set created from the union of two sets, A and B, contains all elements in A plus those elements in B that are not in A.
#     Neither set A nor set B is modified by this operation.
# intersect(setB): Creates and returns a new set that is the intersection of this set and setB. 
#     The set difference, A-B, contains only those elements that are in A but not in B. 
#     Neither set A nor set B is modified by this operation.
# iterator(): Creates and returns an iterator that can be used to iterate over the collection of items.

# Solution:
# List-based implementation. Why?
# The dictionary would seem to be the ideal choice since it can store unique items,
#     but it would waste space in this case, as dictionary stores key/value pairs,
#     which requires two data fields per entry. 
# An array could be used to implement the set, but a set can contain any number of elements,
#     and by definition an array has a fixed size. To use the array structure, we would have to manage
#     the expansion of the array when necessary in the same fashion as it's done for the list.
# Since the list can grow as needed, but list allows for duplicate values, we must make sure as part of the implementation
#     that no duplicates are added to our set.

class Set:
    # Creates an empty set instance.
    def __init__(self):
        self._theElements = list()

    # Returns the number of items in the set.
    def __len__(self):
        return len(self._theElements)

    # Determins if an element is in the set.
    def __contains__(self, element):
        return element in self._theElements

    # Adds a new unique element to the set.
    def add(self, element): 
        if element not in self:
            self._theElements.append(element)

    # Removes an element from the set.
    def remove(set, element):
        assert element in self, "The element must be in the set."
        self._theElements.remove(item)
    
    # Determin if two sets are equal.
    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)
   
    # Determins if this set is a subset of setB
    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True

    # Creates a new set from the union of this set and setB.
    def union(self, setB):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet

    # Creates a new set from the intersection: self set and setB
    def interset(self, setB):
        pass

    # Creates a new set from the difference: self set and setB.
    def difference(self, setB):
        pass

    # Returns an iterator for traversing the list of items.
    def __iter__(self):
        return _SetIterator(self._theElements)

        


if __name__ == "__main__":
    smith = Set()
    smith.add("MATH-121")
    smith.add("ECON-101")

    roberts = Set()
    roberts.add("ANTH-230")
    roberts.add("POL-101")
    smith.add("ECON-101")

    if smith == roberts:
        print("Smith and Roberts are taking the same courses.")
    else:
        sameCoures = smith.intersection(roberts)

