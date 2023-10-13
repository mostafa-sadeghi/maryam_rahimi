def view_menu(dishes):
    result = f'{"dish":<12}{"price":>4}\n'
    for dish, price in dishes.items():
        temp = f"{dish:<12}{str(price):>4}\n"
        result += temp

    return result


def add_new_item(dishes, dish_name, price):
    if dish_name not in dishes:
        dishes[dish_name] = price
    return dishes


def update_existing_item(dishes, dish_name, price):
    if dish_name in dishes:
        dishes[dish_name] = price
    return dishes


def delete_item(dishes, dish_name):
    if dish_name in dishes:
        del dishes[dish_name]
    return dishes


def is_in_dict(dishes, dish_name):
    return dish_name in dishes


def show_orders_summary(orders, menuDict):
    summary = ''
    total = 0
    print('Here is a summary of your order:')
    for order_name, order_amount in orders.items():
        summary += f"- {order_name} : {order_amount}\n"
        total += menuDict[order_name] * order_amount

    return summary, total
