#Date 20/01/2024
# Question : https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

def maxProfit(prices):
    max_profit =0
    
    for i in range(len(prices)):
        if (prices[i] > prices[i-1]):
            max_profit += prices[i] - prices [i-1]
        
    return max_profit

prices = [1, 2, 3, 4, 5]
print(maxProfit(prices))