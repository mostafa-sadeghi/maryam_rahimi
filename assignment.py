# number1

# def validateTicketType(u_i):
#     # if u_i in ('1','2','3'):
#     #     return True
#     if u_i == '1' or u_i == '2' or u_i == '3':
#         return True
#     return False


# print(validateTicketType('1'))  # Expected output: True
# print(validateTicketType('2'))  # Expected output: True
# print(validateTicketType('3'))  # Expected output: True
# print(validateTicketType('4'))  # Expected output: False
# print(validateTicketType('four'))  # Expected output: False
# print(validateTicketType('0'))  # Expected output: False
# print(validateTicketType('-1'))  # Expected output: False

# ticketPrices = [['VIP', 100], ['Standard', 50], ['Child', 25]]
# SoldTickets = [[1, 'Ahmad Ali', 'VIP', 1, 'Standard', 1, 'Child', 1]]
# ticketPrices = [['VIP', 100], ['Standard', 50], ['Child', 25]]

# SoldTickets = []


# def calculateCustomerCost(customerTickets, ticketPrices):
#     counts = customerTickets[3] + customerTickets[5] + customerTickets[7]
#     costs = customerTickets[3] * ticketPrices[0][1] + customerTickets[5] * \
#         ticketPrices[1][1] + customerTickets[7] * ticketPrices[2][1]
#     return (costs, counts)


# def getCustomerPurchase(SoldTickets, ticketPrices):
#     custimer_ticket_count = {
#         'VIP': 0,
#         'Standard': 0,
#         'Child': 0,
#     }
#     customer_name = input("Enter customer name: ")
#     ticket_count = input(
#         f"How many tickets would {customer_name} like to purchase? ")
#     print("Available Ticket Types and Prices:")
#     for index, ticket in enumerate(ticketPrices):
#         print(f'{index + 1}. {ticket[0]} - {ticket[1]} QAR')
#     for i in range(int(ticket_count)):
#         ticket_type = input(f"Choose ticket type for ticket {i+1}:")
#         while not validateTicketType(ticket_type):
#             print("Invalid ticket type, re-enter.")
#             ticket_type = input(f"Choose ticket type for ticket {i+1}:")
#         t_type = ticketPrices[int(ticket_type) - 1][0]
#         custimer_ticket_count[t_type] += 1

#     id = len(SoldTickets) + 1
#     temp_list = [id, customer_name, 'VIP', custimer_ticket_count['VIP'],
#                  'Standard', custimer_ticket_count['Standard'], 'Child', custimer_ticket_count['Child']]
#     SoldTickets.append(temp_list)


# while True:
#     getCustomerPurchase(SoldTickets, ticketPrices)
#     summary = calculateCustomerCost(SoldTickets[-1], ticketPrices)
#     print(f"Order Summary for {SoldTickets[-1][1]}")
#     print("----------------------------------------")
#     print("Customer Name:", SoldTickets[-1][1])
#     print("Number of Tickets:", summary[1])
#     print("Chosen Ticket Types", SoldTickets[-1][2:])
#     print("Total Cost:", summary[0])
#     if input("Do you want to continue? (y n)").lower().startswith("n"):
#         break
# print(SoldTickets)


# number 3


# ticketPrices = [['VIP', 100], ['Standard', 50], ['Child', 25]]
# customerTickets = [1, 'Ahmad Ali', 'VIP', 1, 'Standard', 1, 'Child', 1]
# cost = calculateCustomerCost(customerTickets, ticketPrices)
# print(cost)  # Expected output: (175,3)

# customerTickets = [2, 'Sana Sami', 'VIP', 3, 'Standard', 2, 'Child', 2]
# cost = calculateCustomerCost(customerTickets, ticketPrices)
# print(cost) # Expected output: (450,7)


# def calculateCustomerCost(customerTickets, ticketPrices):
#     counts = 0
#     costs = 0
#     ticket_count = {
#         'VIP': customerTickets[3],
#         'Standard': customerTickets[5],
#         'Child': customerTickets[7],
#     }
#     i = 0
#     for key, value in ticket_count.items():
#         counts += value
#         costs += value * ticketPrices[i][1]
#         i += 1
#     return (costs, counts)


# ticketPrices = [['VIP', 100], ['Standard', 50], ['Child', 25]]
# customerTickets = [1, 'Ahmad Ali', 'VIP', 1, 'Standard', 1, 'Child', 1]
# cost = calculateCustomerCost(customerTickets, ticketPrices)
# print(cost)  # Expected output: (175,3)

# customerTickets = [2, 'Sana Sami', 'VIP', 3, 'Standard', 2, 'Child', 2]
# cost = calculateCustomerCost(customerTickets, ticketPrices)
# print(cost) # Expected output: (450,7)

# def get_max_cost(all_purchase_info):
#     max_cost = 0
#     for item in all_purchase_info:
#         if max_cost < item['cost']:
#             max_cost = item['cost']
#     return max_cost


# def find_winning_customers(All_customers_info, max_cost):
#     winning_customers = []
#     for item in All_customers_info:
#         if item['cost'] == max_cost:
#             winning_customers.append(item['name'])
#     return winning_customers


# def create_all_customers_purchase_info(SoldTickets, ticketPrices):
#     All_customers_info = []
#     for cutomer_ticket in SoldTickets:
#         customer_info = {
#             'name': cutomer_ticket[1],
#             'cost': calculateCustomerCost(cutomer_ticket, ticketPrices)[0],
#         }
#         All_customers_info.append(customer_info)
#     return All_customers_info


# def getWinningCustomers(SoldTickets, ticketPrices):
#     All_customers_info = create_all_customers_purchase_info(
#         SoldTickets, ticketPrices)
#     max_cost = get_max_cost(All_customers_info)
#     winning_customers = find_winning_customers(All_customers_info, max_cost)
#     return (max_cost, winning_customers)


# ticketPrices = [['VIP', 100], ['Standard', 50], ['Child', 25]]
# SoldTickets = [[1, 'Ahmad Ali', 'VIP', 1, 'Standard', 1, 'Child', 1], [
#     2, 'Sana Sami', 'VIP', 2, 'Standard', 0, 'Child', 0]]
# winner = getWinningCustomers(SoldTickets, ticketPrices)
# print(winner)  # Expected output: (200, ['Sana Sami'])
# SoldTickets = [[1, 'Ahmad Ali', 'VIP', 1, 'Standard', 1, 'Child', 1], [2, 'Sana Sami', 'VIP',
#                                                                        2, 'Standard', 0, 'Child', 1], [3, 'Sara Karim', 'VIP', 1, 'Standard', 2, 'Child', 1]]
# winner = getWinningCustomers(SoldTickets, ticketPrices)
# print(winner)  # Expected output: (225, ['Sana Sami', 'Sara Karim'])


# a = int(input("enter a number: "))
# if a % 2 == 0:
#     raise ValueError("blalalal")
# a = int(input("enter a number: "))

# assert (a == 2), f'{a} is not equal to 2'

from unittest import result


def check_if_rectangular_matrix(matrix):
    res = True
    n_rows = len(matrix)
    for row in matrix:
        if len(row) != n_rows:
            res = False
    return res


def get_rectangularmartix_size(first, second):
    if check_if_rectangular_matrix(first) and check_if_rectangular_matrix(second):
        if len(first) == len(second):
            return True
    return False


def matrixAdd(first, second):
    """
    Add two matrices element by element.
    """

    result = []
    for i in range(len(first)):
        temp = []
        for j in range(len(first)):
            temp.append(0)
        result.append(temp)

    if get_rectangularmartix_size(first, second):
        for i in range(len(first)):
            for j in range(len(second)):
                result[i][j] = first[i][j] + second[i][j]

    else:
        raise AssertionError("matrix must be rectangular and smae size")
    return result


print(matrixAdd([[1, 2, 4], [3, 4, 3], [1, 1, 1]],
                [[1, 2, 4], [1, 1, 1], [3, 4, 4]]))
