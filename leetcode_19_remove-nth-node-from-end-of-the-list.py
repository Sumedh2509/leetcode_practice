'''
Given the head of a linked list and an integer n, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4], n = 2

Output: [1,2,4]
Example 2:

Input: head = [5], n = 1

Output: []
Example 3:

Input: head = [1,2], n = 2

Output: [2]
Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #idea/thoughts - we are supposed to break a node , we can probably , iterate thru the whole thing, find the length
        #then length - n and then remove that node 

        array = []
        while head:
            array.append(head) #now we will know number of elements

        array.pop(len(array)- n)

        for i in range(len(array)-1):
            array[i].next = array[i+1]

        return array #scrap this, doesn't work 


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #plan - we will use 2 pointers and make it so that the gap between them is n
        #if the gap betweeen them is n , our left pointer will be at the node that we want to remove when right pointer reaches the end
        #but we want to make the next value of element just before the one we want to remove , the element.next value of what we are removing
        #in order to remove the node, so we create a dummy node
        #this will make it so that out left pointer will be on the node right before the node to be removed

        dummy = ListNode(69 , head) #we don't need value anw, so it can be anything , tho our next val should be head
        #as we want the dummy at the beginning

        left = dummy
        right = head #we will first need to move this pointer , n nodes ahead

        #moving the right pointer to form 
        while n>0 and right: #2nd cond as we might reach the end if the number of nodes are less
            right = right.next
            n -=1

        #moving the right pointer to end now , while left travels behind it
        while right:
            right = right.next
            left = left.next

        #actually removing the node
        left.next  = left.next.next
        return dummy.next #as we don't want that dummy node






