"""
🔥 Best Time to Buy and Sell Stock — Logic Building

Given an array of prices:

prices[i] = stock price on day i.

You must buy first, then sell later.
Goal → maximize profit = sell_price - buy_price
"""


prices = [7, 1, 5, 3, 6, 4]

min_price = float('inf')
max_profit = 0


for price in prices :
    if price < min_price:
        min_price = price

        print("For loooper min price", min_price)

    else:
        profit = price - min_price
        print("For loooper profit", profit)

        if profit > max_profit:
            max_profit = profit
            print("For loooper max profit", max_profit)



print("Maximum Profit:" , max_profit)
