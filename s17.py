# 5 ! = 5 * 4 * 3 * 2 *1
# n! = n*(n-1)* (n-2)....

# factorial = 1
# input_number = int(input('enter a number: '))
# for number in range(input_number,0,-1):
#     factorial *= number

# print(f'factorial of {input_number} is {factorial}')

# Recursive function
# base case
# recursive call


# def factorial(number):
#     if number <= 1:
#         return 1
#     return number * factorial(number - 1)

# for i in range(11):
#     print(f'{i}! = {factorial(i)}')

# import statistics

# var = statistics.pvariance([1,3,4,2,6,5,3,4,5,2])
# print(var)
# std = statistics.pstdev([1,3,4,2,6,5,3,4,5,2])
# print(std)


# from array import array
# import sys

# x = array('i', [1, 2, 3])
# print(x[0])
# print(sys.getsizeof(x))


# string1 = b''
# string2 = u''
# print(type(string1))
# print(type(string2))


# list1 = [10,20,30]
# list2 = [40,50]

# output = list1 + list2
# print(output)
# list1.extend(list2)
# list1.append(list2)
# print(list1)

# def my_func(x):
#     x.append(11)
#     print(x)

# my_func(list1)
# print(list1)


# x = 4

# def my_func(y):
#     y += 1
#     print("y is:",y)

# my_func(x)
# print("x is:",x)


# a_tuple = ('red',)

# print(type(a_tuple))

# for i in range(3):
#     a_tuple += ('green',)


# print(a_tuple)

# my_sequence = ('one', [98, 85, 87])
# first_item, second_item = my_sequence
# print(first_item)
# print(second_item)

# first, second = 'hi'
# print(first)
# print(second)

# x = range(5)
# first, second, *others = x
# print(first)
# print(second)
# print(others)

# number1 = 99
# number2 = 22
# temp = number1
# number1 = number2
# number2 = temp
# number1, number2 = (number2, number1)

# print(number1)
# print(number2)

# colors = ['red', 'green', 'blue']
# print(list(enumerate(colors)))
# for index, value in enumerate(colors):
#     print(f'{index}: {value}')


numbers = [19, 3, 15, 7, 11]

print('Creating a bar chart from numbers:')
print(f'Index{"Value":>8}   Bar')
for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8}    {"*"* value}')
