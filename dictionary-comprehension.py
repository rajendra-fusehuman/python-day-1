'''Given two lists one containing keys and another containing values, create a dictionary
 using dictionary comprehension
'''

def perform_dict_comprehension(keys, values):
    if len(keys) != len(values):
        return ValueError("Error! Different lengths of keys and values")

    new_dictionary = {keys[i]: values[i] for i in range(len(keys))}
    return new_dictionary

keys = ['a', 'b', 'c', 'd']
values = [10, 20, 30, 40]
print(perform_dict_comprehension(keys, values))


'''Given a dictionary with students' names as keys and their respective scores as
 values, create a new dictionary that contains only the students who scored more than
  80 using dictionary comprehension.
'''
old_dict = {'a': 10, 'b': 20, 'c': 88, 'd': 90, 'e': 97}
new_dict = {key: value for key, value in old_dict.items() if value > 80}
print(new_dict)


'''Create a dictionary using dictionary comprehension to represent the ASCII values
 of lowercase alphabets (a-z) where the keys are the alphabets, and the values are
  their corresponding ASCII values
'''
def generate_ascii_dict(alphabets):
    dict_with_ascii = {alphabet: ord(alphabet) for alphabet in alphabets}
    return dict_with_ascii

print(generate_ascii_dict(['a', 'b', 'c', 'd', 'e']))
