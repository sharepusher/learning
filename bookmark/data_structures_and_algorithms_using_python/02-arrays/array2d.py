# Array2D(nrows, ncols): Creates a two-dimensional array organized into rows and columns. 
#      The nrows and ncols arguments indicate the size of the table. The individual elements of the table are initialized to None.

# numRows(): Returns the number of rows in the 2D array

# clear(value): Clears the array by setting each element to the given value.

# getitem(i1, i2): Returns the value stored in the 2D array element at the position indicated by the 2tuple(i1, i2), 
#      both of which must be within the valid range. Accessed using the subscript operator: y = x[1, 2].

# setitem(i1, i2, value): Modifies the contents of the 2D array element indicated by the 2tuple(i1, i2) with the new value.
# Both indices must be within the valid range. Accessed using the subscript operator: x[0, 3] = y

class Array2D:
    # Creates a 2D array of size numRows x numCols.
    def __init__(self, numRows, numCols):
        # Create a 1D array to store an array reference for each row.
        self._theRows = Array(numRows)
    
    # Create the 1D arrays for each row of the 2D array.
    for i in range(numRows):
        self._theRows[i] = Array(numCols)

    # Returns the number of rows in the 2D array.
    def numRows(self):
        return len(self._theRows)

    # Clears the array by setting every element to the given value.
    def clear(self, value):
        for row in range(self.numRows()):
            row.clear(value)

     # Gets the contents of the element at position[i, j]
     def __getitem__(self, ndxTuple):
         assert len(ndxTuple) == 2, "Invalid number of array subscripts."
         row = ndxTuple[0]
         col = ndxTuple[1]
         assert row >= 0 and row < self.numRows() \
             and col >= 0 and col < self.numCols(), \
                 "Array subscript out of range."
         the1dArray = self._theRows[row]
         return the1dArray[col]

     # Sets the contents of the element at position [i, j] to value.
     def __setitem__(self, ndxTuple, value):
         assert len(ndxTuple) == 2, "Invalid number of array subscripts."
         row = ndxTuple[0]
         col = ndxTuple[1]
         assert row >= 0 and row < self.numRows() \ 
             and col >= 0 and col < self.numCols(), \
                 "Array subscript out of range."
         the1dArray = self._theRows[row]
         the1dArray[col] = value


