stock_prices_yesterday = [5,4,3,1,11,0,2]


def get_max_profit4(arr):

    min_price = arr[0]
    max_profit = arr[1] - arr[0]

    for index, current_price in enumerate(arr):

        if index == 0:
            continue

        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)

    return max_profit


print(get_max_profit4(stock_prices_yesterday))




def get_max_profit3(arr):

    if arr.__len__() < 2: return float('-inf')

    # starts checking second to last since we need to buy before selling
    i, v = min(enumerate(arr[:-1]), key=lambda tup: tup[1])

    # maximum of where we can sell in the rest of the list
    profit = max(arr[i + 1:]) - v

    # check if we could have bought before the actual minimum for a bigger profit
    return max(profit, get_max_profit3(arr[:i]))


print(get_max_profit3(stock_prices_yesterday))



def get_max_profit2(arr):

    if arr == []: return 0

    i, v = min(enumerate(arr), key=lambda tup: tup[1])
    profit = max(arr[i:]) - v

    return max(profit, get_max_profit2(arr[:i]))


print(get_max_profit2(stock_prices_yesterday))

# naive:
def get_max_profit_old(arr):
    profit = []
    for i, v in enumerate(arr):
        profit += [max(map(lambda x : x - v, arr[i:]))]
    return max(profit)


print(get_max_profit_old(stock_prices_yesterday))

