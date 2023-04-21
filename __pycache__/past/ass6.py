prices = ['Libya', 0.03, 'Africa', 'Turkey', 1.64, 'Asia', 'Qatar', 0.58, 'Asia', 'Angola', 0.37, 'Africa',
          'Nigeria', 0.42, 'Africa', 'Finland', 2.66, 'Europe', 'Venezuela', 0.02, 'South America',
          'UK', 2.33, 'Europe']


def listOilPricesBelowAveragePrice(prices, AveragePrice):
    print(f'\nCountries with gasoline prices below {AveragePrice} USD dollar:')
    print('-------------------------------------------------------------------------\n')
    for i in range(len(prices)):
        if type(prices[i]) == float and prices[i] > AveragePrice:
            print(
                f'{prices[i-1]} ({prices[i+1]}) gasoline price = {prices[i]}')


def reportAvgOilPrice(prices):
    prices_values = []
    for item in prices:
        if type(item) == float:
            prices_values.append(item)

    average = sum(prices_values)/len(prices_values)
    print(
        f'The average price of gasoline is {average} Dollars per liter.')
    listOilPricesBelowAveragePrice(prices, average)


reportAvgOilPrice(prices)
