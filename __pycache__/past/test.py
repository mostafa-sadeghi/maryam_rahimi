# n = input('> ').title()
# print(n)
print(f'''--------------------------------------------------
{"Country":<14}{"Oil Price":^14}{"Continent":>14}
--------------------------------------------------''')
prices = ['iran', 111.0, 'Asia', 'iran', 2222.0, 'Asia']
for i in range(len(prices)):
    if i % 3 == 0:

        print()
        print(prices[i], end='')
    else:
        print(prices[i], end='')
