'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]

Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:

1 <= prices.length <= 100
0 <= prices[i] <= 100

'''
#thought/ideas - we can obviously do a brute force solution - 
# keep a variable initally having 0 value and loop throught each value as pivot and compare it with that and return that value in the end?
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        for i in range(len(prices)):
            for j in range(i+1 , len(prices)-1):
                profit = max(profit, prices[j] - prices[i])
        return profit


#best solution


#we gonna slide da window
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l ,  r = 0 , 1 #setting up two pointers next to each other
        maxp = 0  #to sotre
        while r < len(prices):  #whie while we aren't done going through the entire array
            if prices[l] < prices[r]:  #comparing prices
                profit = prices[r] - prices[l] #profit
                maxp = max(maxp, profit) 
            else:    #if we ever find a lower price , we put our left pointer to that point
                l = r
            r+=1  #updating the value of r

        return maxp

