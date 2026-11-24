#koko eating bananas 

#core idea is to use binary search 
#you basically found the rate, record that rate and compare while u used binary search 
#the max rate can only be what is max of pile as it is said the answer does exist 
#so we apply binary search from 0  to max(piles)


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)

        while l <= r:
            k = (l+r)//2
            hours = 0 

            for pile in piles:
                hours += (pile +k -1)/k

            if hours <= h:
                res = k 
                r = k - 1 
            else:
                l = k + 1
        return res



            
            