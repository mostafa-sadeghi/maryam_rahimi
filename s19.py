# products = [
#     ("p1", 10),
#     ("p2", 5),
#     ("p5", 600),
#     ("p3", 100),
#     ("p4", 1000)
# ]


# def sort_by_price(product):
#     return product[1]


# products.sort(key=sort_by_price)
# products.sort(key=lambda product:product[1])
# print(products)


# lambda function
# lambda parametrs :Expression

# numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

# odd_numbers = [n for n in numbers if n % 2 !=0]
# print(odd_numbers)

# def is_odd(x):
#     return x % 2 != 0
# result = list(filter(is_odd, numbers))
# result = list(filter(lambda x: x % 2 != 0, numbers))
# result.sort()
# print(result)


# map function

# new_numbers = list(map(lambda x: x ** 2, numbers))
# print(new_numbers)


# products = [
#     ("p1", 10),
#     ("p2", 5),
#     ("p5", 600),
#     ("p3", 100),
#     ("p4", 1000)
# ]


# filtered_products = list(filter(lambda product: product[1] > 100, products))
# print(filtered_products)
# for i in range(len(filtered_products)):
#     print(filtered_products[i])
# print("salam".count('a'))


# numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
# squared_odd_numbers = map(
#     lambda x: x ** 2,    filter(lambda x: x % 2 != 0, numbers))

# print(list(squared_odd_numbers))

# list comprehension
# [expression for item in items]
# odd_numbers = [number**2 for number in numbers if number % 2 != 0]
# print(odd_numbers)


# products = [
#     ("p1", 10),
#     ("p2", 5),
#     ("p5", 600),
#     ("p3", 100),
#     ("p4", 1000)
# ]

# expensive_products = filter(lambda x : x[1]>= 600, products)
# print(list(expensive_products))
# expensive_products = [pr for pr in products if pr[1] >= 600]
# print(expensive_products)
# expensive_products = [pr for pr in products if pr[1] >= 600]
# print(expensive_products)

# zip function

# product_names = ("p1", "p2", "p3")
# products_prices = (10, 100, 1000)
# # [("p1",10), ("p2", 100), ("p3", 1000)]
# print(list(zip(product_names, products_prices)))

# print(list(zip("abc", product_names, products_prices)))

# stack    LIFO

# product_names_1 = ["p1", "p2", "p3"]
# product_names_1.append("p4")
# print(product_names_1)
# print(product_names_1.pop())
# print(product_names_1)

# print('Red'<'orange')
# print(ord('R'))
# print(ord('o'))
# colors = ['Red', 'orange', 'Yellow', 'green', 'Blue']

# print(min(colors, key=lambda s: s.lower()))
# print(max(colors, key=lambda s: s.lower()))

# numbers  = [10,3,7,1,9,4,2,8,5,6]
# reversed_numbers = [item for item in reversed(numbers)]
# print(reversed_numbers)

# names = ['Bob', 'Sue', 'Alex']
# grade = [2, 3, 1]
# for name, grade in zip(names, grade):
#     print(f'Name = {name}, Grade = {grade}')


# import matplotlib.pyplot as plt
# import numpy as np
# import random
# import seaborn as sns

# rolls = [random.randrange(1, 7) for i in range(600)]
# values, frequencies = np.unique(rolls, return_counts=True)

# title = f'Rolling a six-sided Die {len(rolls)} times'

# sns.set_style('whitegrid')
# axes = sns.barplot(x=values, y=frequencies)
# axes.set_title(title)
# axes.set(xlabel='Die value', ylabel='Frequency')
# for bar, f in zip(axes.patches, frequencies):
#     x = bar.get_x() + bar.get_width()/2
#     y = bar.get_height()
#     axes.text(x, y, f, fontsize=10, ha='center')


# plt.show()


# my_variable = {}
# print(type(my_variable))
# my_variable = {1, 2, 3, 4, 5}
# print(type(my_variable))


# my_variable = {
#     'Iran': 'IRI',
#     'United States': 'USA'

# }
# print(my_variable['Iran'])

# print(len(my_variable))
# if len(my_variable):
#     print("Not empty")
# if len(my_variable) != 0:
#     print("Not empty")
# if my_variable:  # {}  []  ()   ''   0   None
#     print("Not empty")

# my_variable.clear()
# print(my_variable)


days_per_month = {
    'Jan': 10,
    'Feb': 20,
}

