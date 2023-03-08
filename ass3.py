def findLowestPrice(prices):
    lowest_prices = []
    lowest_price = prices[0][1]
    for record in prices:
        if record[1] == lowest_price:
            lowest_prices.append(record)
        elif record[1] < lowest_price:
            lowest_price = record[1]
            lowest_prices.clear()
            lowest_prices.append(record)
    countries = sorted([country[0] for country in lowest_prices])
    return "\n".join(countries)


prices = [['Libya', 0.03, 'Africa'],
          ['Turkey', 1.64, 'Asia'],
          ['Qatar', 0.58, 'Asia'],
          ['Angola', 0.37, 'Africa'],
          ['Nigeria', 0.42, 'Africa'],
          ['Finland', 2.66, 'Europe'],
          ['Venezuela', 0.02, 'South America'],
          ['Algeria', 0.02, 'Africa'],
          ['UK', 2.33, 'Europe']]

result = findLowestPrice(prices)
print(result)
