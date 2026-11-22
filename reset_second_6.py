#car fleet question

#in the question we had to convert stuff into time 
#the core logic was , that if the car in front required more time than the car behind it 
#it means they will form a fleet as the car behind will catch up


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair = [(p,s) for ]
        pair = []
        for i in range(len(position)):
            pair.append((position[i], speed[i]))
        stack = []
        pair.sort(reverse=True)
        for p, s in pair:
            stack.append((target-p)/s)

            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        

