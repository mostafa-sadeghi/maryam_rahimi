"""

[1, 2, 3, 4, 5, 6, 7, 8]     True    [1,5,2,6,3,7,4,8]
[1, 2, 3, 4, 5, 6, 7, 8]     False   [5,1,6,2,7,3,8,4]


"""


# def my_function(items, out=False):
#
#     length_half = len(items)//2
#     new_items = []
#     first_half = items[:length_half]
#     second_half = items[length_half:]
#     print("first_half",first_half)
#     print("second_half",second_half)
#
#     for i in range(length_half):
#         if out:
#             new_items.append(first_half[i])
#             new_items.append(second_half[i])
#         else:
#             new_items.append(second_half[i])
#             new_items.append(first_half[i])
#
#     return new_items
#
#
# print("new_items",my_function([1,2,3,4], True))


# def my_function():
#     numbers = []
#     for i in range(100):
#         if i % 5 == 0 or i % 7 == 0:
#             numbers.append(i)
#
#     return numbers, sum(numbers)
#
#
# print("actual numbers:", my_function()[0])
# print("summ of numbers:", my_function()[1])


def my_function():
    return sum([i for i in range(100) if i % 5 == 0 or i % 7 == 0])


print("actual numbers:", my_function())