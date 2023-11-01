# #task1.1
# try:
#    word = str(input())
#    word_letters = list(word.lower())  

#    print("Created list is:")
#    print(word_letters) 
# except ValueError:
#    print('error')

# #task1.2
# try:
#    from collections import Counter
#    word = str(input())
#    word_letters = list(word.lower())

#    letters_count = Counter(word_letters)
#    letters_counts = list(letters_count.items())

#    print(letters_counts)

# except ValueError:
#    print('error')

# #task1.3
# try:
#    from collections import Counter
#    word = str(input())
#    word_letters = list(word.lower())
#    letters_count = Counter(word_letters)

#    list_vows = []
#    list_cons = []
#    list_sym = []

#    for item, count in letters_count.items():
#       if item in 'aeiou':
#          list_vows.append((item, count))
#       elif item.isalpha():
#          list_cons.append((item, count))
#       else:
#          list_sym.append((item, count))

#    print("list_vow =", list_vows)
#    print("list_cons =", list_cons)
#    print("list_sym =", list_sym)

# except ValueError:
#    print('error')

# #task1.4
# def divide_into_quartiles(lst):
#    sorted_list = sorted(lst)
#    list_length = len(sorted_list)
#    q1_length = q2_length = q3_length = q4_length = list_length // 4

#    if list_length % 4 != 0:
#       extra = 4 - list_length % 4
#       q1_length += extra  

#    q1 = sorted_list[:q1_length]
#    q2 = sorted_list[q1_length: q1_length + q2_length]
#    q3 = sorted_list[q1_length + q2_length: q1_length + q2_length + q3_length]
#    q4 = sorted_list[q1_length + q2_length + q3_length:]

#    print("q1 =", q1)
#    print("q2 =", q2)
#    print("q3 =", q3)
#    print("q4 =", q4)

# try:
#    user_input = input("Enter a list of numbers separated by spaces: ")
#    input_list = list(map(int, user_input.split()))

#    if len(input_list) >= 4:
#       divide_into_quartiles(input_list)
#    else:
#       print("Please enter a list with at least 4 numbers")

# except ValueError:
#    print('Error')

# #task 2.1
# try:
#    name = str(input('Student name: '))
#    assignments = input('scores for assignments: ')
#    assignments_scores = list(map(int, assignments.split()))
#    labs = input('labs: ')
#    labs_scores = list(map(float, labs.split()))
#    tests = input('tests: ')
#    tests_scores = list(map(float, tests.split()))

#    student = {
#       'name': name,
#       'assignment': assignments_scores,
#       'test': tests_scores,
#       'lab': labs_scores,
#    }

#    print(student)
# except ValueError:
#    print('error')

# # task 2.2
# try:
#    name = str(input('Student name: '))
#    assignments = input('scores for assignments: ')
#    assignments_scores = list(map(int, assignments.split()))
#    labs = input('labs: ')
#    labs_scores = list(map(float, labs.split()))
#    tests = input('tests: ')
#    tests_scores = list(map(float, tests.split()))

#    if len(assignments_scores) == 4 and len(labs_scores) == 2 and len(tests_scores) == 2:
#       print(f'{name}: 6')
#    else:
#       print('submitted not all activities')
# except ValueError:
#    print('error')

# # task 2.3
# try:
#    name = str(input('Student name: '))
#    assignments = input('scores for assignments: ')
#    assignments_scores = list(map(int, assignments.split()))
#    labs = input('labs: ')
#    labs_scores = list(map(float, labs.split()))
#    tests = input('tests: ')
#    tests_scores = list(map(float, tests.split()))

#    submission_rate = len(assignments_scores) + (len(labs_scores) * 0.5) + (len(tests_scores) * 0.5)

#    def calcalate_final_grade(assignments_scores, labs_scores, tests_scores, submission_rate, name):

#       if submission_rate >= 4:
#          average_assignments = sum(assignments_scores) / len(assignments_scores)
#          average_labs = sum(labs_scores) / len(labs_scores)
#          average_tests = sum(tests_scores) / len(tests_scores)
#          final_grade = (0.3 * average_assignments) + (0.5 * average_labs) + (0.2 * average_tests)
#       elif len(labs_scores) == 0 or len(tests_scores) == 0 or len(assignments_scores) == 0:
#          final_grade = 0
#       else:
#          final_grade = 0

#       student = {
#          'name': name,
#          'assignment': assignments_scores,
#          'test': tests_scores,
#          'lab': labs_scores,
#          'final_grade': final_grade
#       }
#       print(student)

#    calcalate_final_grade(assignments_scores = assignments_scores, labs_scores = labs_scores, tests_scores = tests_scores, submission_rate = submission_rate, name = name)

# except ValueError:
#    print('error')

# # task 2.4
# try:
#    def calcalate_final_grade(assignments_scores, labs_scores, tests_scores, submission_rate, name):
#       if submission_rate >= 4:
#          average_assignments = sum(assignments_scores) / len(assignments_scores)
#          average_labs = sum(labs_scores) / len(labs_scores)
#          average_tests = sum(tests_scores) / len(tests_scores)
#          final_grade = (0.3 * average_assignments) + (0.5 * average_labs) + (0.2 * average_tests)
#       elif len(labs_scores) == 0 or len(tests_scores) == 0 or len(assignments_scores) == 0:
#          final_grade = 0
#       else:
#          final_grade = 0

#       return create_student_dictionary(name=name, assignment=assignments_scores, test=tests_scores, lab=labs_scores, final_grade=final_grade)

#    def create_student_dictionary(name, assignment, test, lab, final_grade):
#       return {
#          'name': name,
#          'assignment': assignment,
#          'test': test,
#          'lab': lab,
#          'final_grade': final_grade
#       }

#    students = {}
#    num_students = int(input("Enter the number of students: "))
#    for i in range(num_students):
#       name = str(input('Student name: '))
#       assignments = input('scores for assignments: ')
#       assignments_scores = list(map(int, assignments.split()))
#       labs = input('labs: ')
#       labs_scores = list(map(float, labs.split()))
#       tests = input('tests: ')
#       tests_scores = list(map(float, tests.split()))

#       submission_rate = len(assignments_scores) + (len(labs_scores) * 0.5) + (len(tests_scores) * 0.5)

#       student_data = calcalate_final_grade(assignments_scores = assignments_scores, labs_scores = labs_scores, tests_scores = tests_scores, submission_rate = submission_rate, name = name)
#       students[student_data['name']] = student_data

#    print("students =", students)
# except ValueError:
#    print('error')

# #task 3.1
# try:
#    transactions = [
#       (1001, 2),
#       (1001, 1),
#       (1003, 2),
#       (1005, 2),
#       (1001, 3),
#       (1007, 1),
#       (1007, 2),
#       (1100, 2),
#       (1003, 2),
#       (1001, 1)
#    ]
#    stats = {}

#    for user, transaction in transactions:
#          if user not in stats:
#             stats[user] = {
#                1: 0,
#                2: 0,
#                3: 0,
#                'mft': 0,
#                'lft': 0
#             }
#          stats[user][transaction] += 1

#    for user, user_stats in stats.items():
#          max_transaction = max(user_stats, key=user_stats.get)
#          min_transaction = min(user_stats, key=user_stats.get)
#          user_stats['mft'] = max_transaction
#          user_stats['lft'] = min_transaction

#    print("stats =", stats)
# except ValueError:
#    print('error')

