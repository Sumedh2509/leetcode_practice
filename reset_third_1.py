class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r =  1, max(piles)

        res = r 
        while l<r:
            hours = 0 
            k = (l+r)//2
            for pile in piles:
                hours += (pile+k-1)/k

            if hours<=h:
                res = k 
                r-=1  
            else:
                l+=1 

        return res
