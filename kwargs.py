'''Write a Python function calculate_total_cost that calculates the total cost of items purchased from a store. The function should accept multiple keyword arguments, where the key
 is the item name, and the value is the item's price.
  The function should return the total cost of all items.
'''

def calculate_total_cost(**items_purchased):
    total_cost = 0
    for item, price in items_purchased.items():
        total_cost += price

    return total_cost

print(calculate_total_cost(monitor=20000, watch=15000, charger=500))


'''Create a function create_student_report that takes the student's name as the
first argument, the student's age as the second argument, and an arbitrary number
 of keyword arguments for the subjects and their respective scores. The function
  should return a dictionary with the student's information and a list of subjects
  along with their scores.
'''

def create_student_report(name, age, **subjects):
    subjects_all = [subject for subject, score in subjects.items()]
    scores_all = [score for subject, score in subjects.items()]

    return {
        "name": name,
        "age": age,
        "subjects": subjects_all,
        "scores": scores_all
    }

print(create_student_report("rajendra", 22, maths=95, physics=94, chemistry=90))
