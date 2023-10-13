# number1

def validateTicketType(u_i):
    # if u_i in ('1','2','3'):
    #     return True
    if u_i == '1' or u_i == '2' or u_i == '3':
        return True
    return False


# print(validateTicketType('1'))  # Expected output: True
# print(validateTicketType('2'))  # Expected output: True
# print(validateTicketType('3'))  # Expected output: True
# print(validateTicketType('4'))  # Expected output: False
# print(validateTicketType('four'))  # Expected output: False
# print(validateTicketType('0'))  # Expected output: False
# print(validateTicketType('-1'))  # Expected output: False

ticketPrices = [['VIP', 100], ['Standard', 50], ['Child', 25]]
SoldTickets = [[1, 'Ahmad Ali', 'VIP', 1, 'Standard', 1, 'Child', 1]]


def getCustomerPurchase(SoldTickets, ticketPrices):
    custimer_ticket_count = {
        'VIP': 0,
        'Standard': 0,
        'Child': 0,

    }
    customer_name = input("Enter customer name: ")
    ticket_count = input(
        f"How many tickets would {customer_name} like to purchase? ")
    print("Available Ticket Types and Prices:")
    for index, ticket in enumerate(ticketPrices):
        print(f'{index + 1}. {ticket[0]} - {ticket[1]} QAR')
    for i in range(int(ticket_count)):
        ticket_type = input(f"Choose ticket type for ticket {i+1}:")
        while not validateTicketType(ticket_type):
            print("Invalid ticket type, re-enter.")
            ticket_type = input(f"Choose ticket type for ticket {i+1}:")
        t_type = ticketPrices[int(ticket_type) - 1][0]
        custimer_ticket_count[t_type] += 1

    id = len(SoldTickets) + 1
    temp_list = [id, customer_name, 'VIP', custimer_ticket_count['VIP'],
                 'Standard', custimer_ticket_count['Standard'], 'Child', custimer_ticket_count['Child']]
    SoldTickets.append(temp_list)


while True:
    getCustomerPurchase(SoldTickets, ticketPrices)
    if input("Do you want to continue? (y n)").lower().startswith("n"):
        break
print(SoldTickets)
