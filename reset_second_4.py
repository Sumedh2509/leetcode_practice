#valid paranthesis 
#the core idea in stack was to storing stuff and popping as we found their pair 
#we add opening brackets only 
#then pop them when we come across a bracket that closes it 



class Solution:
    def isValid(self, s: str) -> bool:

        hashmap = {"}":"{", "]":"[", ")":"("}
        stack = []

        for char in s:
            if char in hashmap:
                if stack and stack[-1] == hashmap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False
