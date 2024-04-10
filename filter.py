'''Implement a function called filter_prime_numbers that takes a list of integers
 as input and uses the filter function to return a new list containing only the prime numbers.
'''
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5)+1):
        if number%i == 0:
            return False
    return True

def filter_prime_numbers(integers):
    return list(filter(is_prime, integers))

print(filter_prime_numbers([1, 2, 13, 15, 17]))


'''Write a Python function filter_long_strings that takes a list of strings as input
 and uses the filter function to return a new list containing strings with more than
  5 characters.
'''
def is_more_than_5(string):
    if len(string) > 5:
        return True
    else:
        return False

def filter_long_strings(strings):
    return list(filter(is_more_than_5, strings))

print(filter_long_strings(["hello", "abc", "fusemachines", "baneshwor"]))
