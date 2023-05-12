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

product_names_1 = ["p1", "p2", "p3"]
