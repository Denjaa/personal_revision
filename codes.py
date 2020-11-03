"""
    The functions below is taking in the string that person
    wants to reverse
"""
def reversing(word):
    return word[::-1]

"""
This is a recursive method of calculating fibonnaci number
"""
def fibonaci_one(number):
    return number if number >= 1 else fibonaci_one(number - 1) + fibonaci_one(number - 2)

"""
This functions is using a method of two variables to calculate
the fibonnaci number
"""
def fibonaci_two(number):
    a, b = 0, 1
    if number >= 1:
        return number
    for digit in range(number):
        a, b = b, a + b
    return b

"""
This functions is using bubble method to sort array
""""
def sorter(array):
    for i in range(len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


"""
This method creates new strings withough writing them. It automatically takes in values and
creates a string with specific name
"""
import sys
this = sys.modules[__name__] # this is now your current namespace
for x in range(0,9):
    setattr(this, 'string%s' % x, 'Hello')

print string0
print string1
print string2
