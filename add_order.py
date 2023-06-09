from s23 import menuDict
from collections import defaultdict
from utils import is_in_dict, show_orders_summary
customer_orders = defaultdict(int)
while True:
    order_name = input('What would you like to order? or "exit" ')
    if order_name == "exit":
        res = show_orders_summary(customer_orders, menuDict)
        print(res[0])
        print(res[1])
        break
    res = is_in_dict(menuDict, order_name)
    if not res:
        print(f"We do not sell {order_name}. Please choose something else.")
        continue
    amount = int(input(f"How much {order_name} would you like? "))
    customer_orders[order_name] += amount
