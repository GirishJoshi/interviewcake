"""
Writing programming interview questions hasn't made me rich yet ... so I might give up and start 
trading Apple stocks all day instead.

First, I wanna know how much money I could have made yesterday if I'd been trading Apple stocks all day.

So I grabbed Apple's stock prices from yesterday and put them in a list called stock_prices, 
where:

* The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
* The values are the price (in US dollars) of one share of Apple stock at that time.

So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

Write an efficient function that takes stock_prices and returns the best profit I could have made 
from one purchase and one sale of one share of Apple stock yesterday.

For example:

  stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
# Returns 6 (buying for $5 and selling for $11)

No "shorting"—you need to buy before you can sell. Also, you can't buy and sell in the same 
time step—at least 1 minute has to pass.

"""

"""
At each iteration, our max_profit is either:

the same as the max_profit at the last time step, or
the max profit we can get by selling at the current_price
How do we know when we have case (2)?

The max profit we can get by selling at the current_price is simply the difference 
between the current_price and the min_price from earlier in the day. 
If this difference is greater than the current max_profit, we have a new max_profit.

So for every price, we’ll need to:

keep track of the lowest price we’ve seen so far
see if we can get a better profit
"""

# stock_prices = [10, 7, 5, 8, 11, 9]
stock_prices = [10, 9, 7, 3, 1]


def get_max_profit_enum(stock_prices):

    max_profit = min(stock_prices) - max(stock_prices)

    for i, price in enumerate(stock_prices[:-1]):

        profit = max(stock_prices[i + 1 :]) - price

        if profit > max_profit:
            max_profit = profit

    return max_profit


def get_max_profit(stock_prices):

    if len(stock_prices) < 2:
        raise ValueError("Require at least 2 prices to find profit.")

    # We'll greedily update min_price and max_profit, so we initialize them at first price
    # and first possible profit
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for current_price in stock_prices[1:]:

        # See what our profit would be if we bought at min_price and sold at current price
        potential_profit = current_price - min_price

        # Update max_profit if we can do better
        max_profit = max(potential_profit, max_profit)

        # Update the min_price so it's always the lowest price we have seen so far
        min_price = min(min_price, current_price)

    return max_profit


print(get_max_profit(stock_prices))
