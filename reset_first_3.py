#the core idea was to use bucket sort 
#you created buckets, the buckets started from 0  to length of the list
#then put the numbers which had that freq in that bucket 
#then use a loop 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  #this is to store the frequencies 
        buckets = [[] for i in range(len(nums) + 1)]

        #counting frequency 
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        #filling the buckets
        for val , freq in count.items():
            buckets[freq].append(val)

        #making the final list by iterating from end
        res = []
        for i in range(len(buckets)-1 ,0, -1 ):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
            