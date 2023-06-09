from colorama import Fore, Back, Style
from utils import view_menu, add_new_item, update_existing_item, delete_item
menuDict = {'soup': 12, 'salad': 15,
            'hummus': 10, 'fattoush': 13, 'tabbouleh': 17,
            'musakhan': 32, 'maqluba': 28, 'mansaf': 40,
            'kibbeh': 52, 'kebab': 45, 'mandi': 34, 'biryani': 25,
            'pizza': 19, 'burger': 22, 'fries': 12,
            'kunefe': 15, 'cheesecacke': 23, 'brownie': 21}
if __name__ == '__main__':
    while True:
        print(f'''
        {Back.BLUE} {"view menu ->":<24} {"1":>5} {Style.RESET_ALL}
        {Back.GREEN} {"add new item ->":<24} {"2":>5} {Style.RESET_ALL}
        {Back.CYAN} {"update existing item ->":<24} {"3":>5} {Style.RESET_ALL}
        {Back.RED} {"delete item ->":<24} {"4":>5} {Style.RESET_ALL}
        {Back.RED} {"Exit ->":<24} {"0":>5} {Style.RESET_ALL}
        ''')
        user_input = input('> ')
        if user_input == '1':
            res = view_menu(menuDict)
            print(res)

        elif user_input == "2":
            dish_name = input('enter dish name: ')
            price = input('enter dish price: ')
            menuDict = add_new_item(menuDict, dish_name, price)
            print("operation completed")

        elif user_input == "3":
            dish_name = input('enter dish name: ')
            price = input('enter dish price: ')
            menuDict = update_existing_item(menuDict, dish_name, price)
            print("operation completed")

        elif user_input == "4":
            dish_name = input('enter dish name: ')
            menuDict = delete_item(menuDict, dish_name)
            print("operation completed")

        elif user_input == '0':
            exit()
