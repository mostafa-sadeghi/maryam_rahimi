# python primitive types: numbers   str    bool

# int   float   complex

# x = 1
# print(type(x))

# x = 1.5
# print(type(x))
# x = 1 + 2j
# print(type(x))


# str

# x = ''
# print(type(x))
# x = ""
# print(type(x))


# x = 'abcs'
# print(len(x))

# message = 'he said, "some thing"'
# message = "he said, \"some thing\""
# message = 'welcome. \npython from zero to hero!'
# message = '''welcome.
# python from zero to hero!'''
# message = '''he said, "some thing"'''
# print('first\tsecond')
# print('hi.\rwelcome to our python class.\rwelcome to our pygame')
# print('hello.\rhi')

# name = "artin"
# course = "django"
# message = "hello %s, welcome to our %s class." % (name, course)
# print(message)
# message = "hello " + name + ", welcome to our " + course + " class."
# print(message)
# print("hello", name+", welcome to our", course,  "class.")
# message = f"hello {name}, welcome to our {course} class."

# name = input('enter your name: ')
# print(type(name))
# course = input('enter your course: ')
# print("hello", name+", welcome to our", course,  "class.")

# n1 = int(input('enter first number: '))  # or float
# n2 = int(input('enter second number: '))
# print(f'{n1} + {n2} = {n1 + n2}')

# //
# print(3/2)
# print(3//2)
# %
# print(5 %2)
# **
# str1 = '*'
# print(str1 * 9)

# string = 'abcdefghi'
# print(string[0])
# print(string[1])
# print(string[2])

# print(string[:])
# print(string[:3])
# print(string[0:3])

# def
# ghi
# efghi
# abcd

# print(string[::2])


# numbers = '123456789'
# print(numbers[::2])
# print(numbers[1::2])

# my_list = [1, 'a', [1, 2]]
# print(my_list[-1][0])
# print(my_list[-1][1])

# my_list = [-1, 2, [[3], [], [0, 1, 2, 16]]]
# # print(my_list[-1][2][3])
# my_list.append(34)
# print(my_list)

# del my_list[2]
# print(my_list)

# my_list.remove(2)
# print(my_list)
# numbers = [1, 2, 3, 4, 5, 2, 4]
# numbers.remove(2)

# print(numbers.count(2))
# numbers.insert(1, 333)
# print(numbers)
# print(numbers.index(333))


# list1 = [1, 2, 3, 4]
# list2 = [4, 5, 6, 7]

# print(list1 + list2)


# print([list1] * 5)

# numbers = (1, 2, 3, 4, 5, 6, 7)  # immutable
# print(type(numbers))
# print(numbers[0])
# print(numbers[::2])
# numbers[0] = 122  # error tuple object does not support item assignment
# tupple doesn't have append and so on ...
# dict dictionary

# favorite_sports = {
#     'arman': 'football',
#     'sara': 'tennis',
#     'tina': 'baseball'
# }

# print(favorite_sports)
# print(f"tina likes {favorite_sports['tina']}")
# favorite_sports['sima'] = 'football'
# favorite_sports['sara'] = 'football'
# print(favorite_sports)
# del favorite_sports['arman']
# print(favorite_sports)

# import math
# print(round(2.9))
# print(round(2.6))
# print(round(2.5))
# print(round(2.4))
# print(abs(-1.7))
# print(math.ceil(2.2))
# print(math.floor(2.2))
