class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        # as answer does always exist the highest rate will be the highest value that exists in our pilies array
        # we can simply try the range of 1 to our max of pile to find the best rate, brute force method
        # we can then just apply binary search on that range 

        l, r = 1 , max(piles) 
        res = r
        while l<=r:
            k = (l+r)//2
            hours = 0 #setting up a varaible to count the number of hours
            for pile in piles:
                # hours += math.ceil(pile/k)
                hours += (pile + k-1)//k #this is the method round up 

            

            if hours <= h:  #we using = as it is alright if we finish it exactly in given time 
                res = k  #finding the minimum
                r = k-1

            else:
                l = k+1
            
        return res
