def nonNegativeFloatValidation(prompt, errorMessage):
    number = input(prompt)
    try:
        float_number = float(number)
        if float_number > 0:
            return float_number
        else:
            print(errorMessage)
            return nonNegativeFloatValidation(prompt, errorMessage)

    except Exception as ex:
        print(errorMessage)
        return nonNegativeFloatValidation(prompt, errorMessage)


def readOilPrices(prices, noOfCountries):
    valid_continent = ['Asia', 'Africa', 'Europe',
                       'North America', 'South America', 'Australia', 'Antarctica']

    for i in range(int(noOfCountries)):
        country = input(f'enter the name of country {i+1}: ')
        price = nonNegativeFloatValidation(
            f"Enter the oil price in '{country}': ", 'The number of countries must be a positive number greater than zero. ')

        continent = ''
        while continent not in valid_continent:
            continent = input(
                f"{country} is located in which continent?: ").title()

        prices.append(country)
        prices.append(price)
        prices.append(continent)

    return prices


num_of_countries = nonNegativeFloatValidation(
    'Enter the number of countries: ', 'The number of countries must be a positive number greater than zero. ')
prices = readOilPrices([], num_of_countries)

print(prices)


def listOilPrices(prices):
    string = ''

    string += f'--------------------------------------------------\n{"Country":<14}{"Oil Price":^14}{"Continent":>14}\n--------------------------------------------------\n'

    for price in prices:
        string += f'{price[0]:<14}{price[1]:^14}{price[2]:>14}\n'
    string += '\n--------------------------------------------------'
    ########################## NOTE : ANOTHER WAY###########################
#     string += f'''--------------------------------------------------
# {"Country":<14}{"Oil Price":^14}{"Continent":>14}
# --------------------------------------------------\n'''

#     for price in prices:
#         string += f'{price[0]:<14}{price[1]:^14}{price[2]:>14}\n'
#     string += '\n--------------------------------------------------'
    return string


output = listOilPrices(prices)
print(output)
