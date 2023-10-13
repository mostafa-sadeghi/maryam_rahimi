# menuDict = {'soup': 12, 'salad': 15,
#             'hummus': 10, 'fattoush': 13, 'tabbouleh': 17,
#             'musakhan': 32, 'maqluba': 28, 'mansaf': 40,
#             'kibbeh': 52, 'kebab': 45, 'mandi': 34, 'biryani': 25,
#             'pizza': 19, 'burger': 22, 'fries': 12,
#             'kunefe': 15, 'cheesecacke': 23, 'brownie': 21}

# message = '''
# Welcome to restaurant management system
# 1: view menu
# 2: add new item
# 3: update existing item
# 4: delete item
# 0: exit
# '''


# def add_new_menu_item(name, price):
#     '''
#     This function is used to add new menu item to dict
#     name : str,
#     price : str,
#     Returns : None
#     '''

#     menuDict[name] = price


# while True:
#     print(message)
#     operation = input("Which operations do you want to perform (0 to 4)? ")
#     if operation == '0':
#         print('Goodbye!')
#         break
#     elif operation == '1':
#         for key, value in menuDict.items():
#             print(f'{key:<20}{value:^4}')
#             # key_length = len(key)
#             # while key_length < 20:
#             #     key += ' '
#             #     key_length += 1
#             # print(key, value)

#     elif operation == '2':
#         item_name = input('What item would you like to add? ')
#         item_price = input(f'What is the price of {item_name}? ')
#         add_new_menu_item(item_name, item_price)

#     elif operation == '3':
#         item_name = input('What item would you like to update? ')
#         if item_name in menuDict:
#             item_price = input(f'What is the price of {item_name}? ')
#             add_new_menu_item(item_name, item_price)
#         else:
#             print(
#                 f'{item_name} is not in the menu. If you want to add it, select operation 2.')

#     elif operation == '4':
#         item_name = input('What item would you like to remove?')
#         if item_name in menuDict:
#             del menuDict[item_name]
#         else:
#             print(
#                 f'{item_name} is not in the menu. If you want to add it, select operation 2.')

from random import choices, randint
import string
def randomLetter():
    lowercase_letters = string.ascii_lowercase
    # x = randint(1,26)
    # return lowercase_letters[x]


    # # return ''.join(choices(lowercase_letters, k=3))
    # res = ''
    # x = choices(lowercase_letters, k=3)
    # for s in x:
    #     res += s
    # return res


# print("our random lowercase letter is:", randomLetter())
