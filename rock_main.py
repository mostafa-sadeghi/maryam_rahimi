from random import choice
from rock_config import GAME_CHOICES, RULES, scoreboard


def get_user_choice():
    user_input = input("Enter your choice (r, p, s): ")
    if user_input not in GAME_CHOICES:
        print("wrong choice, try again please ...")
        return get_user_choice()
    return user_input


def get_system_choice():
    return choice(GAME_CHOICES)




def find_winner(user:str, system:str)->str:
    """
    This function is used for finding winner
    :param user
    :param system
    :return: winner
    """
    match = {user, system}
    if len(match) == 1:
        return None
    return RULES[tuple(sorted(match))]
    





def play():
    result = {'user': 0, 'system': 0}
    while result['user'] < 3 and result['system'] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner = find_winner(user_choice, system_choice)
