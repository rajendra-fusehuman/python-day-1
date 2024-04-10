''' Write a Python function that takes an arbitrary number of positional arguments
 and returns the sum of all the numbers. Test your function with various input cases.'''

def sum(*args):
    total = 0
    for arg in args:
        total += arg

    return total

print(sum(1,2,3.5,4,5,6))


'''Write a Python function concat_strings that
 takes any number of strings as arguments and returns a single concatenated string.'''

def concat_strings(*strings):
    concatenated_string = ""
    for string in strings:
        concatenated_string += string

    return concatenated_string

print(concat_strings("rajendra", "baskota"))
