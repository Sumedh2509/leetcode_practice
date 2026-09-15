'''
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.

Example 1:

Input: target = 10, position = [1,4], speed = [3,2]

Output: 1
Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

Example 2:

Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

Output: 3
Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there are 3 car fleets that will arrive at the destination.

Constraints:

n == position.length == speed.length.
1 <= n <= 100,000
0 < target <= 1,000,000
1 <= speed[i] <= 1,000,000
0 <= position[i] < target
All the values of position are unique.
'''


#idea-  cars behind just have the role of catching up to the car ahead of it
# u can just call the whole fleet one car (since we just wanna return the number of fleets)
# those cars who catch up with the car in front of em -they will attain the speed of the car they caught up to
# we can pop the data of these cars, in the end the length of our stack will be our answer
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        #above line is similar to 
        '''pair = []
        for i in range(len(position)):
            pair.append((position[i], speed[i]))'''
        pair.sort(reverse=True) #sorting in reverse
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s) # (target-p)/s is time required for the car to reach the target

            #if time of the car in front is greater than time of the car in back--> the car in back will catch up to car in front
            #so they will form a fleet 


            while len(stack) >= 2 and stack[-1] <= stack[-2]: #checking the length of stack
                #and top of stack , is less than or equal to the car behind it 
                stack.pop()
        return len(stack)


    # pair = [(p, s) for p, s in zip(position, speed)]
    #         #above line is similar to 
    #         '''pair = []
    #         for i in range(len(position)):
    #             pair.append((position[i], speed[i]))'''