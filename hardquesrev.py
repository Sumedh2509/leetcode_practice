
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we are supposed to make buckets and also count frequency and then fill those bucket
        #and then go through those buckets 
        #creating buckets 
        buckets = [[] for i in range(len(nums)+1)] 
        #counting frequencies 
        freq = {} 
        for num in nums: 
            freq[num] = 1 + freq.get(num, 0)
        #filling up the buckets 
        for val , ind in freq.items():
            buckets[ind].append(val)
        res = []
        for i in range(len(buckets)-1, 0 , -1):
            for vals in buckets[i]:
                res.append(vals)
                if len(res) == k:
                    return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #creating hashmap
        freq = [[] for i in range(len(nums) + 1)] #creates a 2d list

        for num in nums:
            count[num] = 1 + count.get(num, 0) #get the value of num in dict and add one to it or if it doesn't exists give 0 so that its frequency will be 1
        for num, cnt in count.items(): #if u use only count it only gives keys , with .items() it gives key value pair
            freq[cnt].append(num)#at the cnt index (the location of list in our 2d list) append this number

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res



#core idea was to find the time 
#if the car ahead required more time than the car behind 
#it just meant that they will form a fleet 


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        for i in range(len(position)-1):
            combined.append((position[i], speed[i]))

        combined.sort(reverse=True)

        stack = []
        for pos , spee in combined:
            time = (target-pos)/spee
            stack.append(time)

            while len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack) 

        


        

