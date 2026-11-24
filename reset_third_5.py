#this was about sliding the window 


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0 ,1 
        maxp = 0 

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxp = max(maxp , profit)
                
            else:
                l = r 
            r+=1 
        return maxp 
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0 
        res = 0 

        for r in range(len(s)):

            while s[r] in seen:
                seen.remove[s[l]]
                l += 1 
            seen.add(s[r]) 
            res = max(res, r - l + 1)
        return len(res)
