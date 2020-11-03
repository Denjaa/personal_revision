def reversing(word):
    return word[::-1]

def fibonaci_one(number):
    return number if number >= 1 else fibonaci_one(number - 1) + fibonaci_one(number - 2)

def fibonaci_two(number):
    a, b = 0, 1
    if number >= 1:
        return number
    for digit in range(number):
        c = a + b
        a, b = b, c
    return b

def sorter(array):
    for i in range(len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
