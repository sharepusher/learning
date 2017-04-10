# About Gregorian calandar and Julian calendar.
# Gregorian calendar was introduced in the year 1582 by Pope Gregory XIII to repalce the Julian Calendar.
# The new calendar corrected the miscalculation of the lunar year and introduced the leap year.
# The official first date of the Gregorian calendar is Friday, October 15, 1582.
# The proleptic Gregorian calendar is an extension for accommodating earlier dates with the first date on Nov 24, 4713 BC.
# This extension simplifies the handling of dates across older calendars and its use can be found in many software applications.


# Defining the date ADT
# A date represents a single day in the proleptic Gregorian calendar in which the first day starts on November 24, 4713 BC
# 
# Date(month, day, year): Creates a new Date instance initialized to the given Gregorian date which must be valid.
# Year 1 BC and earlier are indicated by negative year components. 
# day(): Returns the Gregorian day number of this date.
# month(): Returns the Gregorian month number of this date.
# year(): Returns the Gregorian year of this date.
# monthName(): Returns the Gregorian month name of this date.
# dayOfWeek(): Returns the day of the week as a number between 0 and 6 with 0 representing Monday and 6 representing Sunday.
# numDays(otherDate): Returns the number of days as a positive integer between this date and the otherDate.
# isLeapYear(): Determins if this date falls in a leap year and returns the appropriate boolean value.
# advancedBy(days): Advances the date by the given number of days. 
#                   The date is incremented if days is positive and decremented if days is negative. 
#                   The date is capped to Nov24, 4714 BC, if necessary.
# comparable(otherDate): Compares this date to the otherDate to determin their logical ordering. 
#                        This comparison can be done using any of the logical operators <, <=, >, >=, ==, !=
# toString(): Returns a string representing the Gregorian date in the format mm/dd/yyyy. 
#             Implemented as the Python operator that is automatically called via the str() constructor.



# After defining the ADT, we need to provide an implementation. 
# 1) Date representation/Data structure:  There are two common approaches to storing a date in an object.

#    One approach stores the three components - month, day, and year, as three separate fields.
#    With this format, it's easy to access the individual components, but it's difficult to compare two dates
#    or to compute the number of days between two dates since the number of days in a month varies from month to month.

#    The second approach stores the date as an integer value representing the Julian day, 
#    which is the number of days elapsed since the initial date of November 24, 4713 BC(using the Gregorian calendar notation).

# 2) How to constructing date in Julian day

# NOTE: Python does not provide a technique to protest attributes and helper methods in order to prevent their use outside the class definition.
# In this text, we use identifier names, which begin with a single underscore to flag those attributes and methods that should be considered protected and rely on the user of the class to not attempt a direct access.


#data structure that provides basic date operation.
# Implements a prolecptic Gregorian calendar date as a Julian day number.

class Date:
    # Create an object instance for the specified Gregorian date
    def __init__(self, month, day, year):
        self._julianDay = 0
        assert self._isValidGregorian(month, day, year), \
               "Invalid Gregorian date."
        # The first line of the equation, T = (M-14) / 12, has to be changed
        # since Python's implementation of integer division is not the same as the mathematical definition.
        tmp = 0
        if month < 3:
            tmp = -1
        self._julianDay = day - 32075 + \
                (1461 * (year+4800+tmp) // 4) + \
                (367 * (month-2-tmp*12) // 12) - \
                (3 * ((year+4900+tmp)//100) // 4)
        
        # Extracts the appropriate Gregorian date component.
        def month(self):
            return (self._toGregorian())[0] # returning M from (M, d, y)

        def day(self):
            return (self._toGregorian())[1] # returning D from (m, D, y)
       
        def year(self):
            return (self._toGregorian())[2] # returning Y from (m, d, Y)

        # Returns day of the week as an int between 0(Mon) and 6(Sun).
        def dayOfWeek(self):
            month, day, year = self._toGregorian()
            if month < 3:
                month = month + 12
                year = year - 1
            return ((13*month+3) // 5 + day + \
                    year + year//4 - year//100 + year//400) % 7

        # Returns the date as a string in Gregorian format.
        def __str__(self):
            month, day, year = self._toGregorian()
            return "%02d/%02d/%04d" % (month, day, year)

        # Logically compares the two dates.
        def __eq__(self, otherDate):
            return self._julianDay == otherDate._julianDay
   
        def __lt__(self, otherDate):
            return self._julianDay < otherDate._julianDay

        def __le__(self, otherDate):
            return self._julianDay <= otherDate._julianDay

        # The remaining methods are to be included at this point.
        # TODO

        # Returns the Gregorian date as a tuple: (month, day, year).
        def _toGregorian(self):
            A = self._julianDay + 68569
            B = 4 * A // 146097
            A = A - (146097*B + 3) // 4
            year = 4000 * (A+1) // 1461001
            A = A - (1461*year // 4) + 31
            month = 80 * A // 2447
            day = A - (2447*month // 80)
            A = month // 11
            month = month + 2 - (12*A)
            year = 100 * (B-49) + year + A
            return month, day, year

    def _isValidGregorian(self, month, day, year):
        if not month or not day or not year:
            return False
        if not str(month).isdigit() or not str(day).isdigit() or not str(year).isdigit():
            return False
        # TODO
        return True 
