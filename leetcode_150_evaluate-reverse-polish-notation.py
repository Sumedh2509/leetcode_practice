'''
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
Constraints:

1 <= tokens.length <= 10000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-200, 200].

'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] #intialzing stack
        for i in tokens: #iterating thru the tokens

            #checking conditions 
            #stack.pop() - remember the top value gets popped first 
            if i == "+": 
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                a,b = stack.pop() , stack.pop()
                stack.append(b-a)
            elif i == "*":
                stack.append(stack.pop()*stack.pop())
            elif i == "/":
                a,b = stack.pop(), stack.pop()
                #we are doing the following thing cuz python truncates towards negative if the integers are negative
                stack.append(b//a if (b*a>0) else -(abs(b)//abs(a)))
                #use of ternary operator, cond1 if b*a>0 (similar sign for both)
            else:
                stack.append(int(i))
        return stack[0]