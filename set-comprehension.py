'''Given a list of numbers, create a set using set comprehension that contains
only unique even numbers.
'''
def set_comprehension(numbers):
    set = {number for number in numbers}
    print(type(set))
    return set

print(set_comprehension([1,1,345,45,6,345]))


'''Given a list of words, write a Python program to create a set using set
 comprehension that contains all the unique characters present in the words.
'''
def words_to_unique_char(words):
    set = {char for word in words for char in word}
    return set

words = ["apple", "banana", "orange"]
print(words_to_unique_char(words))


'''Given two strings, write a Python program to create a set using set comprehension
 that contains all the characters that are common in both strings.
'''
def set_with_common_words(str1, str2):
    set = {char for char in str1 if char in str2}
    return set

print(set_with_common_words("apple", "orange"))
