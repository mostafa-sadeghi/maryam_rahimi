# numbers = [1, 2, 3, 44, 2, 3, 44, 1, 2]

# define a function that takes a list as a parameter and return True if list items are unique
# otherwise return False

# print(set(numbers))
# numbers_one = [1,2,3,4]
# numbers_two = [1,4,3,2]
# print(numbers_one == numbers_two)
# a = {}
# print(type(a))

# students = {
#     'id': 1,
#     'name': 'sara'
# }
# print(type(students))

# numbers_one = {1, 2, 3, 4, 4}
# numbers_two = {1, 4, 3, 2}
# print(type(numbers_one))
# print(numbers_one == numbers_two)


# numbers = [1, 2, 3]
# numbers = [1, 2, 3, 44, 2, 3, 44, 1, 2]
# status = True
# i = 0
# while i < len(numbers):
#     if not status:
#         break
#     j = i + 1
#     while j < len(numbers):
#         if numbers[i] == numbers[j]:
#             print(i, j, numbers[i], False)
#             status = False
#             break
#         j += 1

#     i += 1
# if status:
#     print(True)


# status = True
# for i in range(len(numbers)):
#     if not status:
#         break
#     for j in range(i+1,len(numbers)):
#         if numbers[i] == numbers[j]:
#             print(i,j,numbers[i],False)
#             status = False
#             break
# else:
#     print(True)


# def is_unique(numbers):
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             if numbers[i] == numbers[j]:
#                 return (i, j, numbers[i], False)
#     return True


# print(is_unique(numbers))


# def is_unique(items):
#     if list(set(items)) == items:
#         return True
#     return False

# print(is_unique(numbers))


# exercise 2 :
'''
Let s be a string that contains a sequence of decimal numbers separated by commas,
e.g., s = '1.23,2.4,3.123'. Write a program that prints the sum of the numbers in s.

'''

# numbers = input('enter numbers as a sequence like `1,2,3,4.1` : ')
# print(type(numbers))
# print(numbers.split(','))

'''
Write a program that asks the user to input 10 integers, and then prints the largest
odd number that was entered. If no odd number was entered, it should print a message to that effect.
'''

# max_number = 0
# for i in range(5):
#     number = int(input('enter an integer number:> '))
#     if number % 2 != 0 and number > max_number:
#         max_number = number

# if max_number == 0:
#     print("no odd number enterd!")
# else:
#     print(max_number)


# print(max([1,2,3]))


'''
Write a program that examines three variables—x, y, and z—and prints the largest
odd number among them. If none of them are odd, it should print a message to that effect

'''
x = int(input('enter an int number: '))
y = int(input('enter an int number: '))
z = int(input('enter an int number: '))


# first condition: all numbers are even
if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    print("all numbers are even!!!")

elif x % 2 == 0 and y % 2 == 0 and z % 2 != 0:
    print("largest odd number is:", z)
elif x % 2 == 0 and z % 2 == 0 and y % 2 != 0:
    print("largest odd number is:", y)
elif z % 2 == 0 and y % 2 == 0 and x % 2 != 0:
    print("largest odd number is:", x)
elif x % 2 == 0:
    if y > z:
        print("largest odd number is:", y)
    else:
        print("largest odd number is:", z)
elif y % 2 == 0:
    if x > z:
        print("largest odd number is:", x)
    else:
        print("largest odd number is:", z)
elif z % 2 == 0:
    if y > x:
        print("largest odd number is:", y)
    else:
        print("largest odd number is:", x)

else:
    if x > y and x > z:
        print("largest odd number is:", x)
    elif y > z:
        print("largest odd number is:", y)
    else:
        print("largest odd number is:", z)
