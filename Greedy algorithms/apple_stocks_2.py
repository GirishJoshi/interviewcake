stock_prices = [10, 7, 5, 4, 3, 1]


def get_max_profit(stock_prices):

    if len(stock_prices) < 2:
        raise ValueError("Need at least 2 prices to get profit")

    lowest = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for current_price in stock_prices[2:]:

        potential_profit = current_price - lowest

        max_profit = max(potential_profit, max_profit)

        lowest = min(lowest, current_price)

    return max_profit


print(get_max_profit(stock_prices))
