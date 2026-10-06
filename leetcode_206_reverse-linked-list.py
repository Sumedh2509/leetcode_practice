'''
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]

Output: [3,2,1,0]
Example 2:

Input: head = []

Output: []
Constraints:

0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):

          #these are instance variables
#         self.val = val  # every object u create will have its value and something that it is pointing to
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            temp = curr.next #this will be lost when we reverse the node , so we gotta store it in temp
            curr.next = prev #pointing behind/in the opposite direction 
            prev = curr #we are incrementing the values, prev becomes what our current is 
            curr = temp #curr becomes what we stored in temp . which was the natural next node before
        return prev #at some point, curr will become none as we keep incrementing it , at that time prev will be the last element of our original linked list, and as we are reversing
    # naturally our head 

