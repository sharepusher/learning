# Student File Reader ADT
# Extract student records from external storage. 

# StudentFileReader(filename): Creates a student reader instance for extracting student records from the given file.
#     The type and format of the file is dependent on the specific implementation.

# open(): Opens a connection to the input source and prepares it for extracting student records.
#     If a connection cannot be opened, an exception is raised.

# close(): Closes the connection to the input source. If the connection is not currently open, an exception is raised.

# fetchRecord(): Extracts the next student record from the input source and returns a reference to a storage object containing the data.
#    None is returned when there are no additional records to be extracted. 
#    An exception is raised if the connection to the input source was previously closed.

# fetchAll(): The same as fetchRecord(), but extracts all student records(or those remaining) from the input source and returns them in a python list.        

# Avoid the use of tuples when storing structured data since it's better practice to use classes with named fields.
# You may notice there is only a constructor with no additonal methods. 
# This is a complete class as defined and represents a storage class.
# The constructor is all that's needed to define the two data fields for storing the two component values.

# NOTE: Storage class should be defined withtin the same module as the class with which they will be used.
# Some storage classes may be intended for internal use by a specific class and not meant to be accessed from outside the module.
# In those cases, the name of the storage class will begin with a single underscore, which flags it as being private to the module.

class StudentFileReader:
    # Create a new student reader instance.
    def __init__(self, inputSrc):
        self._inputSrc = inputSrc
        self._inputFile = None

    # Open a connection to the input file.
    def open(self):
        self._inputFile = open(self._inputSrc, "r")
   
    # Close the connection to the input file.
    def close(self):
        self._inputFile.close()
        self._inputFile = None

    # Extract all student records and store them in a list.
    def fetchAll(self):
        theRecords = list()
        student = self.fetchRecord()
        while student != None:
            theRecords.append(student)
            student = self.fetchRecord()
        return theRecords

    # Extract the next student record from the file.
    def fetchRecord(self):
        # Read the first line of the record.
        line = self._inputFile.readline()
        if line == "":
            return None

        # If there is another record, create a storage object and fill it.
        student = StudentRecord()
        student.idNum = int(line)
        student.firstName = self._inputFile.readline().rstrip()
        student.lastName = self._inputFile.readline().rstrip()
        student.classCode = int(self._inputFile.readline())
        student.gpa = float(self._inputFile.readline())
 
        return student


 
# Storage class used for an individual student record.
class StudentRecord:
    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0

    

