grades = ["A", "B", "C", "D", "E", "F", "A", "C"]


def grade_frequency(grades):
    a_count, b_count, c_count, d_count, f_count = (0, 0, 0, 0, 0)
    output = {}
    for grade in grades:
        if grade == "A":
            a_count += 1
        elif grade == "B":
            b_count += 1
        elif grade == "C":
            c_count += 1
        elif grade == "D":
            d_count += 1
        elif grade == "F":
            f_count += 1
    output["A"], output["B"], output["C"], output["D"], output["F"] = (
        a_count, b_count, c_count, d_count, f_count)
    return output, a_count + b_count + c_count + d_count + f_count


print(grade_frequency(grades))

# grades = ["A", "B", "C", "D", "E", "F", "A", "C"]

# def grade_frequency(grades):
#     output = {}
#     for grade in grades:
#         output[grade] = grades.count(grade)

#     return output, sum(output.values())


# print(grade_frequency(grades))

# grades = ["A", "B", "C", "D", "E", "F", "A", "C"]

# from collections import Counter
# def grade_frequency(grades):
#     output = Counter(grades)
#     total = sum(output.values())
#     return output, total
# print(grade_frequency(grades))


# my_dict = {}
# id = 1
# name = "Sara"
# my_dict[id] = 1
# my_dict[name] = "Sara"
# print(my_dict)
