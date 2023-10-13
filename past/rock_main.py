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


def find_winner(user: str, system: str) -> str:
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


def update_scoreboard(result):
    if result['user'] == 3:
        scoreboard['user'] += 1
        msg = 'You Win'
    else:
        scoreboard['system'] += 1
        msg = 'You Lose'

    print('#' * 50)
    print('##',f'user: {scoreboard["user"]}')
    print('##',f'system: {scoreboard["system"]}')
    print('##',f'last game: {msg}')
    print('#' * 50)



def play():
    result = {'user': 0, 'system': 0}
    while result['user'] < 3 and result['system'] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner = find_winner(user_choice, system_choice)
        if winner == user_choice:
            msg = 'You Win'
            result['user'] += 1
        elif winner == system_choice:
            msg = 'You lose'
            result['system'] += 1
        else:
            msg = "BLALAL"
        print(f"user: {user_choice}\tsystem:{system_choice}\tresult:{msg}")

    update_scoreboard(result)
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == 'y':
        play()


if __name__ == "__main__":
    play()