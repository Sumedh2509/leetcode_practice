'''
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. 
If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example 1:

Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]
Example 2:

Input: temperatures = [22,21,20]

Output: [0,0,0]
Constraints:

1 <= temperatures.length <= 100,000.
1 <= temperatures[i] <= 100

'''

#idea 1- the brute force method , just check everything
#this is a valid solution but way too inefficient O(n^2)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        n = len(temperatures)
        for i in range(n):
            for j in range(i+1 , n):
                if temperatures[j]>temperatures[i]:
                    result.append(j-i)
                    break
                
            else: 
                result.append(0)
        return result

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) #intializing an array with default values of 0
        stack = []  # pair: [index, temp] (kim- this thing stores tupples)

        for i, t in enumerate(temperatures): #enumerating - taking index  and values
            while stack and t > stack[-1][1]: 
                #cheks if stack is not empty (i.e doesn't run on the first iteration)
                #stack[-1] --> top of the stack -->this will point to a tupple
                #stack[-1][1] --> indicates the *2nd* value of tupple (which is value of temp)


                stackInd, stackval = stack.pop() #stackInd = index, stackval = temp , we need to pop those 
                #these popped values are now temporarily stored in stackInd and stackval

                res[stackInd] = i - stackInd  
                #stackInd is basically the index of number we are popping and i is the current index we are on
                #so since we did find the temperature greater than that of the day on top of stack--> t>stack[-1][1]
                # we are finding the distance between the previous top and current instance of higher temp 


            stack.append((i, t))
        return res

'''
temperatures = [73, 74, 71, 76]
ITERATION 3

i = 2
t = 71

Current state:
res = [1, 0, 0, 0]
stack = [(1, 74)]

Check the while condition:
t > stack[-1][1]
71 > 74 → FALSE

Therefore, we DON'T pop anything.
Why? Because 71 is NOT warmer than 74.

Now add the current temperature to the stack:
stack.append((i, t))

stack becomes:
[(1, 74), (2, 71)]

res remains:
[1, 0, 0, 0]
'''