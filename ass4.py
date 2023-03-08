prices = ['Libya', 0.03, 'Africa', 'Turkey', 1.64, 'Asia',
          'Qatar', 0.58, 'Asia', 'Angola', 0.37, 'Africa', 'Nigeria',
          0.42, 'Africa', 'Finland', 2.66, 'Europe', 'Venezuela', 0.02,
          'South America', 'Algeria', 0.02, 'Africa', 'Algeria2', 0.01, 'Africa', 'UK', 2.33, 'Europe', 'Algeria2', 0.02, 'Africa', ]


def findLowestPrice(prices):
    lowest_prices = []
    lowest_price = prices[1]
    for i in range(len(prices)):
        if type(prices[i]) == float:
            if prices[i] == lowest_price:
                lowest_prices.append(prices[i-1])
            elif prices[i] < lowest_price:
                lowest_price = prices[i]
                lowest_prices.clear()
                lowest_prices.append(prices[i-1])

    return "\n".join(lowest_prices)


result = findLowestPrice(prices)
print(result)
