'''
Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.

Example 1:



Input: head = [1,2,3,4], index = 1

Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:



Input: head = [1,2], index = -1

Output: false
Constraints:

0 <= Length of the list <= 1000.
-1000 <= Node.val <= 1000
index is -1 or a valid index in the linked list.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #ideas/thoughts - maybe we can store the elements we visit in an array , and cross check everytime?
        array = []
        curr = head
        while curr: #till we don't iterate thru the entire linked list
            if curr in array:
                return True
            
            array.append(curr)
            curr = curr.next
        return False




#u use two pointers fast and slow, if there exists a cycle both of them are bound to meet 
#imagine a circular track, if one moves with a speed of 2 and one with speed of 1
#if u use concept similar to relative speed in physics, it is clear that they are bound to meet
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast, slow = head,head #setting up fast and slow pointers 
        #this is known as floyd's fast and slow pointer

        while fast and fast.next:  #while fast hasn't reached none, it is gonna reach first anw
            #we are making fast.next aswell , as our fast pointer moves two times
            slow = slow.next #incrementing the value of slow
            fast = fast.next.next #incrementing value of fast
            if slow == fast: #if they encounter each other it means our linked list has a cycle
                return True #so we return true


        return False #or we return false

