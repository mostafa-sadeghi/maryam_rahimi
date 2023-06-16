menuDict = {'soup': 12, 'salad': 15,
            'hummus': 10, 'fattoush': 13, 'tabbouleh': 17,
            'musakhan': 32, 'maqluba': 28, 'mansaf': 40,
            'kibbeh': 52, 'kebab': 45, 'mandi': 34, 'biryani': 25,
            'pizza': 19, 'burger': 22, 'fries': 12,
            'kunefe': 15, 'cheesecacke': 23, 'brownie': 21}


def maxMenu(menu):
    most_expensive = 0
    item = None
    for name, price in menu.items():
        if price > most_expensive:
            most_expensive = price
            item = (name, price)

    return f"The most expensive dish is {item[0]} and it costs {item[1]} QAR."


print(maxMenu(menuDict))
