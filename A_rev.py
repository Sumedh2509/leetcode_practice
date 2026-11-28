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



#the basic idea was to make a rigid window the length of s1 and shift that window 
#u checked the frequency of letters using a hashmap 
s1="adc"
s2="dcda"
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2): return False

        freqs1 = {}
        windowfreq = {}

        #calculating the frequency of letters in s1 and initiallizing our windwo 
        for i in range(n):
            freqs1[s1[i]]  = 1 + freqs1.get(s1[i], 0)
            windowfreq[s2[i]]  = 1 + windowfreq.get(s2[i], 0)

        #moving the window and updating frequency acc to it in in winndowfreq 

        for j in range(n, len(s2)):
            

            #increasing frequency of letter that are coming (in front)
            windowfreq[s2[j]] = 1 + windowfreq.get(s2[j], 0)
            windowfreq[s2[j-n]] -=1 

            if windowfreq[s2[j-n]] == 0:
                del windowfreq[s2[j-n]]
            if freqs1 == windowfreq: return True
        return False


#we know that solution does exists for every given input
#so the worst case would be to eat with rate of max(piles) 
#so we can apply binary search over 1 - max(piles) 
#we will calculate hours it takes for each of the rate and record it 
#whichever will be minimum will be our answer
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        res= 0 #variable to keep track of minimum 

        while l <= r:
            k = (l+r)//2 
            hours = 0 
            for pile in piles:
                hours+= (pile + k-1)//k

            if hours <= h: 
                r = k -1  
            else:
                l = k + 1
            
        return res 
