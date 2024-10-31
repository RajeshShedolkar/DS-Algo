
def cal_max_profit(prices):
    start = prices[0]
    i = 1
    total_profit = 0
    last_stock_vaule = 0
    while i < len(prices):
        if prices[i] > start:
            last_stock_vaule = prices[i]
        else:
            total_profit += last_stock_vaule - start
            start = prices[i]
            last_stock_vaule = prices[i]
        i+=1

    total_profit += last_stock_vaule - start
    print(total_profit)
    return total_profit


prices = [100, 180, 260, 310, 40, 535, 695]
cal_max_profit(prices)
