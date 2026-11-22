# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#the core idea was storing the pointer in a temp variable 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev



        