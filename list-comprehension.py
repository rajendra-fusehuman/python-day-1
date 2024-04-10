'''Given a list of strings, create a new list that contains only the strings with
 more than 5 characters using list comprehension.
'''
def string_concatenation(strings):
    strings_char_more_than_5 = [string for string in strings if len(string) > 5]
    return strings_char_more_than_5

strings = ["hello", "rajendra", "baskota", "fuse", "machines"]


'''Given two lists of integers, create a list that contains the product of each element
 of the first list with the corresponding element in the second list using list comprehension
'''
def perform_product(list_1, list_2):
    if len(list_1) != len(list_2):
        raise ValueError("Please provide lists with same lengths!!")

    product_list = [list_1[i] * list_2[i] for i in range(len(list_1))]
    return product_list

list_1 = [1,2,3,4,5]
list_2 = [2,3,4,5,6]
print(perform_product(list_1, list_2))


'''Given three lists list1, list2, and list3, each containing integers, write a Python
 program using list comprehension to generate a new list of unique triplets (x, y, z)
  where x is from list1, y is from list2, and z is from list3, such that x + y + z = 0.
'''
def triplets_sum_zero(list_1, list_2, list_3):
    triplets = [(x, y, z) for x in list_1 for y in list_2 for z in list_3]
    triplets_with_sum_0 = list(set(triplet for triplet in triplets if sum(triplet)==0))

    return triplets_with_sum_0

list_1 = [-1, 0, 1, 2, -1, -4]
list_2 = [-2, -1, 0, 1, 2]
list_3 = [-1, 0, 1, 2, 3]
result = triplets_sum_zero(list_1, list_2, list_3)
print(result)
