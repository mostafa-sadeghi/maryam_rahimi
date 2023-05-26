# country = {
#     'united States': "USA",
#     "Iran": "IRI"
# }

# country["another"] = "an"
# # country["another"] = "am"
# print(country)


# if country:
#     print("ok")
# else:
#     print("nothing")
# print(len(country))
# country.clear()
# print(country)

# for item in country:
#     print(item)
# for item in country.keys():
#     print(item)
# for item in country.values():
#     print(item)
# for key, val in country.items():
#     print(key, val)


# numbers = [1,2,3,4,5,6]
# numbers2 = [1,2,4,3,5,6]

# print(numbers == numbers2)

# country1 = {
#     'united States': "USA",
#     "Iran": "IRI"
# }
# country2 = {
#     "Iran": "IRI",
#     'united States': "USA",
# }

# print(country1 == country2)

students_grades = {
    'maryam': [92, 100, 90],
    'ali': [82, 100, 60],
    'nima': [62, 100, 80],
}
students = []


def generate_all_students_info(students):
    for item in students_grades.items():
        temp_for_student = {}
        st_ave = sum(item[1])/len(item[1])
        temp_for_student["name"] = item[0]
        temp_for_student["average"] = st_ave
        temp_for_student["failed_course_score"] = []
        temp_for_student["min_score"] = min(item[1])
        temp_for_student["max_score"] = max(item[1])
        for score in item[1]:
            if score < 70:
                temp_for_student["failed_course_score"].append(score)

        students.append(temp_for_student)
    return students
# print(students)


def find_failed_students(students):
    """ find failed student`s name
    :params students
    :returns students
    """
    failed_students = []
    for student in students:
        if student['failed_course_score']:
            failed_students.append(student["name"])
    return failed_students


if "__name__" == "__main__":
    generate_all_students_info(students)
    print(" ".join(find_failed_students(students)))


# students_ave = []
# for item in students_grades.items():
#     temp_for_student = {}
#     st_ave = sum(item[1])/len(item[1])
#     temp_for_student[item[0]]  = st_ave
#     students_ave.append(temp_for_student)

# student_name = input("enter student`s name: ")
# for item in students_ave:
#     if student_name in item:
#         print(item[student_name])
