# message = "hello every body. welcome to python class. python is crossplatform and highlevel language."
# old_word = "python"
# new_word = "java"


# def my_function(message, old_word="", new_word=""):
#     i = 0
#     result = ""
#     while i < len(message):
#         if message[i:i+len(old_word)] == old_word:
#             result += new_word
#             i += len(old_word)

#         else:
#             result += message[i]
#             i += 1
#     return result


# print(my_function(message, old_word, new_word))


# def my_function(totalSeconds):
#     hours = totalSeconds//3600
#     totalSeconds = totalSeconds % 3600
#     minutes = totalSeconds//60
#     seconds = totalSeconds % 60

#     return (str(hours)+'h', str(minutes)+'m', str(seconds)+'s')


# print(my_function(3605)[0], my_function(3605)[1], my_function(3605)[2])

numbers = [28,25,2,28]
print(min(numbers))
def get_smallest(numbers):
    smallest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n

    return smallest

print(get_smallest(numbers))
