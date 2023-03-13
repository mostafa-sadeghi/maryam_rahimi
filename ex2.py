# def is_ascending(numbers):
#     for i in range(len(numbers)-1):
#         if numbers[i] >= numbers[i+1]:
#             return False
#     return True


# print(is_ascending([1, 2, 3, 4, 5]))


# Truthy and Falsy
# "" Falsy    [] Falsy   ()  Falsy  0 Falsy   None Falsy


USERNAME = ('admin', 'root')
PASS = 'root'


# user_name = input('enter user name:> ')
# password = input('enter password:> ')

# if user_name == "" or password == "":
#     print("you must enter user name and password")
# if not (user_name or password):  # if not (bool(user_name) or bool(password))
#     print("you must enter user name and password")

# elif user_name == USERNAME and password == PASS:
#     print("you'r acount is valid")


# if (user_name == 'admin' or user_name == 'root') and password == 'root':
#     print("you'r acount is valid")


# a = 3
# b = 4
# c = 0


# if a < b and c:  # Truthy | Falsy
#     print("1-",'a is lower than b and c')

# if a < b and a < c:
#     print("2-",'a is lower than b and c')

# if a & b: # bitwise and
#     print("ok")


# if 10 == '10':
#     print("equal")

# if "bag" > "apple":
#     print("bag is greater than apple")
# print(ord("b"))
# print(ord("a"))


# success = False

# for i in range(3):
#     print("Attempt")
#     success = True
#     if success:
#         print("success")
#         break
# else:
#     print("attempted 3 times and failed...")


# write a function that recieves a list of numbers and calculates sum of even numbers in the list

# def sum_of_even_numbers(numbers):
#     total = 0
#     for number in numbers:
#         if number % 2 ==0:
#             total += number  # total = total + number
#     return total

# print(sum_of_even_numbers([1,2,3,4,5,6,7,8,9]))


# x = list(range(5))

# print(x)

# y = list('abcdefghi')

# print(y)

# z = list(tuple((1,2,3,4,5)))
# print(z)


# def increment(number, by=1):
#     return number + by

# print(increment(5,2))
# print(increment(5))

# xargs

# def multiply(x,y):
#     print(x*y)


# multiply(2,3)
# multiply(2,3,4) # error


# def multiply(*args):
#     print(args)


# multiply(2,3)
# multiply(2,3,4,5,6,7,8)


# def multiply(*args):
#     total = 1
#     for number in args:
#         total *= number   # total *= number

#     print(total)
# multiply(2,3)
# multiply(2,3,4,5,6,7,8)


# def greet(name, family):
#     return f'hello {name} {family}'


# print(greet(family="rezaei",name="nikan"))


# **args

# def something(**args):
#     print(args)


# something(id=1, name="nikan",family ="blalala")


# x = 0

# def something():
#     global x
#     x += 1


# something()
# something()
# something()

# print(x)


def multiply(*args):
    total = 1
    for number in args:
        total *= number   # total *= number

        return total


print(multiply(2, 3))
print(multiply(2, 3, 4, 5, 6, 7, 8))
