## List Comprehension
# >>> numbers = [1,2,3]
# >>> new_numbers = [n*2 for n in numbers]
# >>> print(new_numbers)
# [2, 4, 6]
# >>> name = "Angela"
# >>> new_name = [letter for letter in name]
# >>> print(new_name)
# ['A', 'n', 'g', 'e', 'l', 'a']
# >>> list = range(1,5)
# >>> new_list = [n*2 for n in list]
# >>> print(new_list)
# [2, 4, 6, 8]
# >>> name = [letter for letter in "Felipe"]
# >>> print(name)
# ['F', 'e', 'l', 'i', 'p', 'e']
# >>> names = ["Felipe", "Carlos", "Quesz", "Venna", "Dom", "Alexis", "Tyler", "Maria"]
# >>> short_names = [name for name in names if len(name) < 6]
# >>> print(short_names)
# ['Quesz', 'Venna', 'Dom', 'Tyler', 'Maria']
# >>> upper_names = [name.upper() for name in names if len(name) > 5]
# >>> print(upper_names)
# ['FELIPE', 'CARLOS', 'ALEXIS']
# >>>

# >>> import random
# >>> names = ["Felipe", "Ace", "Tyranny", "Apollo", "Valentina", "Campbell", "Smitty"]
# >>> student_scores = {name:random.randint(0,100) for name in names}
# >>> print(student_scores)
# {'Felipe': 14, 'Ace': 38, 'Tyranny': 60, 'Apollo': 72, 'Valentina': 85, 'Campbell': 75, 'Smitty': 23}
# >>> passed_students = {name:score for (name,score) in student_scores.items() if score > 70}
# >>> print(passed_students)
# {'Apollo': 72, 'Valentina': 85, 'Campbell': 75}
# >>>

student_dict = {
    "student": ["Felipe", "Apollo", "Artemis", "Valentina"],
    "score": [88, 72, 92, 75],
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)


for (index, row) in student_data_frame.iterrows():
    print(row.student)
    if row.student == "Felipe":
        print(row.score)
