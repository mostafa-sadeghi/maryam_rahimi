# list unpacking

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# n1 = numbers[0]
# n2 = numbers[1]

# first,second, *others = numbers

# print(first)
# print(second)
# first,*others, last = numbers

# print(first)
# print(last)


# x, *n, y, z = numbers

# print(x)
# print(y)
# print(z)

# characters = ["a", "b", "c", "d"]
# for c in characters:
#     print(c)

# for i in range(len(characters)):
#     print(characters[i])


# for item in enumerate(characters):
#     print(item)
#     print(f'number {item[0]} is {item[1]}')
#     string = "number " + item[0] + " is " + item[1]
#     print("number", item[0], "is", item[1])
#     print(f'number {item[0]} is {item[1]}')
# number 0 is 'a'


numbers = [1, 2, 3, 44, 2, 3, 44, 1, 2]
# print(numbers.count(100))
number = int(input('enter a number: '))
counter = 0
for n in numbers:
    if n == number:
        counter += 1
print(f'{number} count : {counter}')
