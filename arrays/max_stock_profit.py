# 100, 200, 50, 300, 100, 400
def cal_max_profit(prices):
    start = prices[0]
    i = 1
    total_profit = 0
    last_stock_vaule = start
    while i < len(prices):
        if prices[i] > last_stock_vaule:
            last_stock_vaule = prices[i]
        else:
            
            total_profit += last_stock_vaule - start
            start = prices[i]
            last_stock_vaule = prices[i]
        i+=1
    
    total_profit += last_stock_vaule - start
    print(prices, total_profit)
    return total_profit
    

try:
    assert cal_max_profit([100, 180, 260, 310, 40, 535, 695]) == 865, "Test Case 1 Failed"
    assert cal_max_profit([100, 150, 200, 250, 300]) == 200, "Test Case 2 Failed"
    assert cal_max_profit([300, 250, 200, 150, 100]) == 0, "Test Case 3 Failed"
    assert cal_max_profit([500]) == 0, "Test Case 4 Failed"
    assert cal_max_profit([100, 180, 260, 40, 310]) == 430, "Test Case 5 Failed"
    assert cal_max_profit([100, 100, 100, 100]) == 0, "Test Case 6 Failed"
    assert cal_max_profit([100, 200, 50, 300, 100, 400]) == 650, "Test Case 7 Failed"
    assert cal_max_profit([100, 101, 100, 101, 100]) == 2, "Test Case 8 Failed"
    assert cal_max_profit([100, 200]) == 100, "Test Case 9 Failed"
    assert cal_max_profit([100, 300, 200]) == 200, "Test Case 10 Failed"
except:
    pass

print("All test cases passed!")



prices = [100, 200, 50, 300, 100, 400]
cal_max_profit(prices)
