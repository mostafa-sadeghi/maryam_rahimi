import random

# frequency1, frequency2, frequency3, frequency4, frequency5, frequency6 = (
#     0, 0, 0, 0, 0, 0)
# frequency1 = frequency2 = frequency3 = frequency4 =frequency5 =frequency6 = 0


# for roll in range(6_000_000):
#     face = random.randrange(1, 7)
#     if face == 1:
#         frequency1 += 1
#     elif face == 2:
#         frequency2 += 1
#     elif face == 3:
#         frequency3 += 1
#     elif face == 4:
#         frequency4 += 1
#     elif face == 5:
#         frequency5 += 1
#     elif face == 6:
#         frequency6 += 1
# print(f'Face{"Frequency":>13}')
# print(f'{1:>4}{frequency1:>13}')
# print(f'{2:>4}{frequency2:>13}')
# print(f'{3:>4}{frequency3:>13}')
# print(f'{4:>4}{frequency4:>13}')
# print(f'{5:>4}{frequency5:>13}')
# print(f'{6:>4}{frequency6:>13}')

# random.seed(32)
# for i in range(10):
#     print(random.randint(1,6), end=' ')


# import random


# def main():
#     die_values = roll_dice()
#     print(display_dice(die_values))
#     sum_of_dices = sum(die_values)
#     if sum_of_dices in (7, 11):
#         game_status = 'WON'
#     elif sum_of_dices in (2, 3, 12):
#         game_status = "LOST"
#     else:
#         game_status = 'CONTINUE'
#         point = sum_of_dices
#         print("point is :", point)

#     while game_status == 'CONTINUE':
#         print('print enter to continue...')
#         input('> ')
#         die_values = roll_dice()
#         print(display_dice(die_values))
#         sum_of_dices = sum(die_values)
#         if sum_of_dices == point:
#             game_status = "WON"
#         elif sum_of_dices == 7:
#             game_status = 'LOST'
#     if game_status == 'WON':
#         print('Player Wins')
#     else:
#         print('Player loses')


# def roll_dice():
#     """Roll two ....."""
#     die1 = random.randrange(1, 7)
#     die2 = random.randrange(1, 7)

#     return (die1, die2)


# def display_dice(dice):
#     die1, die2 = dice
#     return f'Player rolled {die1} + {die2} = {sum(dice)}'


# if __name__ == '__main__':

#     main()


# def rectangle_area(l=2,w=3):
#     print(l * w)

# rectangle_area(2,3)
# rectangle_area()

# print(min(88,75,96,55,83))

# def average(*args):
#     return sum(args)/len(args)

# print(average(90,100))
# print(average(90,100, 80))

# s = 'Hello'

# s.lower()

# scope
# local scope
# global scope

x = 0

def my_func():
    global x
    x += 1
    print(f'{x}')

# my_func()
# my_func()
# my_func()