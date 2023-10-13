import math

# def ouroboros(string) -> bool:
#     """
#     Returns True if first and last chars are the same,
#     this is not the case if chars are upper or lower
#     """
#     pass


# def ramadan1444CashBack(bill):
#     """
#     returns the percentage and amount of the bill that will be given back to customers.
#     """
#
#     if bill % 4 == 0:
#         return (bill, 4, math.ceil(bill * 4/100))
#
#
# data = [("LabTest", 20, 80), ("Assignment", 5, 100)]
# # (25, 84.0)


# def overallGrade(data):
#     x = 0
#     total = 0
#     for datium in data:
#         x += datium[1]
#         total += datium[1] * datium[2]
#     return (x, total/x)
#
#
# print(overallGrade(data))

# ramadanCharity([100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
#                 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
#                 100, 100, 100, 100, 100, 100, 100, 100])

# 1, 5, 10, 50, 100, 200 or 500 QAR

# CURRENCY = (1, 5, 10, 50, 100, 200, 500)
# def ramadanCharity(notes):
#     # if len(notes) != 29 or len(notes) != 30:
#     if len(notes) not in (29, 30):
#         raise AssertionError("Bad days number")
#     currency_counter = {}
#     final_amount = 0
#     increasing_flag = True
#     for c in CURRENCY:
#         currency_counter[c] = 0
#     for i in range(len(notes) - 1):
#         if notes[i] > notes[i + 1]:
#             increasing_flag = False
#
#         if notes[i] in CURRENCY:
#             currency_counter[notes[i]] += 1
#             final_amount += notes[i]
#
#     if notes[i + 1] in CURRENCY:
#         currency_counter[notes[i + 1]] += 1
#         final_amount += notes[i + 1]
#
#         # if note == 1:
#         #     currency_counter[1] += 1
#         # if note == 5:
#         #     currency_counter[5] += 1
#         # if note == 10:
#         #     currency_counter[10] += 1
#         # if note == 50:
#         #     currency_counter[50] += 1
#         # if note == 100:
#         #     currency_counter[100] += 1
#         # if note == 200:
#         #     currency_counter[200] += 1
#         # if note == 500:
#         #     currency_counter[500] += 1
#
#     return currency_counter, final_amount, increasing_flag
#
#
# print(ramadanCharity(
#     [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
#      100, 100, 100, 100, 100, 100]))
# print(ramadanCharity(
#     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 100, 100, 100, 100, 100, 100, 100,
#      100, 100, 100]))
# print(ramadanCharity(
#     [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 100, 100, 100, 100, 100, 100, 100,
#      100, 100, 100]))
# print(ramadanCharity(
#     [100, 100, 100, 100, 10, 100, 100, 10, 200, 50, 200, 5, 5, 500, 200, 200, 100, 50, 10, 5, 1, 200, 10, 500, 100, 10,
#      1, 1, 500, 500]))
# print(ramadanCharity([500]))

numbers = [1, 2, 3, 4, 5, 80, 1, 77, 2, 5, 88, 2, 5, 80, 900, 1, 2, 3, 5, 80]


def my_counter(numbers):
    result = {}
    sum_of_even_counts = 0
    for key in numbers:
        result[key] = numbers.count(key)
        result[key] = 0
    # result = {key:0 for key in numbers}
    for key in numbers:
        result[key] += 1
    return result


print(my_counter(numbers))

# تابعی بنویسید که خروجی تابع قبل را به عنوان پارامتر دریافت نماید
# و مجموع مقادیر زوج و نیز تعداد مقادیر فرد موجد در دیکشنری را نمایش دهد