from functools import reduce

'''Write a Python function calculate_factorial that takes an integer as input and
 uses the reduce function to return the factorial of that number.
'''
def calculate_factorial(number):
    product = reduce((lambda x, y: x * y), list(range(1, number+1)))
    return product

number = 5
print(calculate_factorial(number))


'''Implement a function called concatenate_strings that takes a list of strings
 as input and uses the reduce function to return a single string containing
  the concatenation of all the elements.
'''
def concatenate_strings(strings):
    concatenated_string = reduce((lambda x, y: x + y), strings)
    return concatenated_string

print(concatenate_strings(["rajendra", "baskota", "fuse", "machines"]))
