'''
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:

1 <= s.length <= 1000
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")":"(" , "]":"[", "}": "{"}
        for char in s: 
            if char in hashmap:
                if stack and stack[-1] == hashmap[char]:
                    #the above statement checks if stack is empty and if the last added character to stack matches the value 
                    stack.pop()
                    #we pop that out of the stack if they do match 
                    #note that we aren't adding close brackets into our stack 
                else:
                    return False
                #return False if they do not match 
            
            #this is where elements are added in our stack 
            #it adds the open brackets to our stack , so that the above chunk can later compare
            else:
                stack.append(char)
         #return true if stack is empty        
        return True if not stack else False 
    