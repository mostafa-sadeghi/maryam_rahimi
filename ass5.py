prices = [['Libya', 0.03, 'Africa'],
          ['Turkey', 1.64, 'Asia'],
          ['Qatar', 0.58, 'Asia'],
          ['Angola', 0.37, 'Africa'],
          ['Nigeria', 0.42, 'Africa'],
          ['Finland', 2.66, 'Europe'],
          ['Venezuela', 0.02, 'South America'],
          ['UK', 2.33, 'Europe']]


def listOilPricesBelowAveragePrice(prices, AveragePrice):
    countries_less_than_ave = []
    for record in prices:
        if record[1] < AveragePrice:
            countries_less_than_ave.append(record)
    print(f'\nCountries with gasoline prices below {AveragePrice} USD dollar:')
    print('-------------------------------------------------------------------------\n')
    for country_record in countries_less_than_ave:
        print(
            f'{country_record[0]} ({country_record[2]}) gasoline price = {country_record[1]}')


def reportAvgOilPrice(prices):
    prices_values = []
    for record in prices:
        prices_values.append(record[1])
    average = sum(prices_values)/len(prices_values)
    print(
        f'The average price of gasoline is {average} Dollars per liter.')
    listOilPricesBelowAveragePrice(prices, average)


reportAvgOilPrice(prices)
