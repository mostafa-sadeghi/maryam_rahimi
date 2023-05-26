from s20 import find_failed_students, generate_all_students_info

students_grades = {
    'maryam': [92, 100, 90],
    'ali': [82, 100, 60],
    'nima': [62, 100, 80],
}
students = []
students = generate_all_students_info(students)
failed_students_list = find_failed_students(students)
for st in failed_students_list:
    print(st)