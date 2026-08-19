'''
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in 
O
(
1
)
O(1) time.

Example 1:

Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1
Constraints:

-2^31 <= val <= 2^31 - 1.
pop, top and getMin will always be called on non-empty stacks.
At most 
3
∗
10
4
3∗10 
4
  calls will be made to push, pop, top, and getMin.

'''

#a blueprint of how stack is built using class

#idea- push , pop , top (peek) are the usual stack functions which can be done in O(1) time
# getmin is something that is challenging -we make it happen in O(1) time - by maintaing an extra stack 
#this stack (mistack) will always contain the minimum value 

class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        value = min(value, self.minstack[-1] if self.minstack else value)
        #in above line -we update the value of val so we can put minimum value at that point of time in minstack
        self.minstack.append(value)
        

    def pop(self) -> None:
        #just popping the values -we need to pop from minstack too 
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        #we have to return the top value of stack 
        return self.stack[-1]

    def getMin(self) -> int:
        #we store the min value at top in our extra stack 
        return self.minstack[-1]
        