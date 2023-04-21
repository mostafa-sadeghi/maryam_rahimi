'''
This Program is used to listing all countries oil prices 
'''


def nonNegativeFloatValidation(prompt: str, errorMessage: str) -> float:
    '''
    This function is used for validating non negative float.

    Parameters : 
        prompt : str,
        errorMessage : str
    Returns : float
    '''

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


def readOilPrices(prices: list, noOfCountries: float) -> list:
    '''
    This Function is for reading oil prices

    Parameters:
        prices : 2D List,
        noOfCountries : float

        Returns: 
            prices : 2D List
    '''
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

        prices.append([country, price, continent])

    return prices


num_of_countries = nonNegativeFloatValidation(
    'Enter the number of countries: ', 'The number of countries must be a positive number greater than zero. ')
prices = readOilPrices([], num_of_countries)


def listOilPrices(prices: list) -> str:
    '''
    This Function is used for listing the details of all prices records.

    Paremeters :
        prices : 2D List,

    Returns :
        oilPricesDetails : str
    '''
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
