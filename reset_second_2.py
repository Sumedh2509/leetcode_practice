#3 sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        #iterating thru the entire list
        for ind , val in enumerate(nums):
            if val > 0:
                break   #as nums is sorted there is no way that the addition will ever become 0
            #as the next values will be greater than val

            if ind>0  and nums[ind-1] == val:
                continue

            l ,r = ind+1 , len(nums) - 1
            #going thru the elements succedding our current pivot in for loop
            while l<r:
                threesum = val + nums[l] + nums[r]

                if threesum>0:
                    r-=1
                elif threesum<0:
                    l+=1
                else:
                    res.append([val, nums[l], nums[r]])
                    l+=1
                    r-=1

                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res
            
