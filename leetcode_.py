'''
You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

Example 1:



Input: l1 = [1,2,3], l2 = [4,5,6]

Output: [5,7,9]

Explanation: 321 + 654 = 975.
Example 2:

Input: l1 = [9], l2 = [9]

Output: [8,1]
Constraints:

1 <= l1.length, l2.length <= 100.
0 <= Node.val <= 9
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #idea/thoughts  - 


        dummy = ListNode() #creating a dummy nodee
        cur = dummy #setting curr to dummy
 
        carry = 0   #setting the carry up 
        while l1 or l2 or carry:  #while there is nodes in l1 or l2 or we have a carry (8+5)
            v1 = l1.val if l1 else 0  #if the node exists, take the value , else just use 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry #basic addition
            carry = val // 10  #to find carry 
            val = val % 10     #to find the actual digit that we will have in our  node
            cur.next = ListNode(val) #setting that node up

            # update ptrs
            cur = cur.next   #move the curr pointer
            l1 = l1.next if l1 else None #moving through the list
            l2 = l2.next if l2 else None

        return dummy.next