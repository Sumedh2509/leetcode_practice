'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:



Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]
Example 2:

Input: list1 = [], list2 = [1,2]

Output: [1,2]
Example 3:

Input: list1 = [], list2 = []

Output: []
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        #ideas/thoughts - we can iterate thru the linked lists, first check which head is smaller, let that be the head of our new linked list
        # for what it points to , we again check the elements and just assign head.next to the next element and so on 

        dummy = node = ListNode() #creating a dummy node
        while list1 and list2:
            if list1.val<list2.val:
                node.next= list1 #our node now points to 1 of the 2nd list
                list1 = list1.next #it got assigned so we move to the next
            else: #in any other case do this
                node.next = list2# our node now points to the 
                list2 = list2.next #moving the head of list 2 
            node = node.next #so that the node finally points to none (as it is in a linked list
            
        node.next = list1 or list2 #if there are diff number of elements in lists, like one has 2 and one has 3, once we iterate thru the list 
        #which has 2 elements , list 2 will have 1 element left for which there will be no execution of our loop
        #but we do know that as the lists are sorted it will just be in increasing order, so we just append it at the end

        return dummy.next #we are returning everything that is next to dummy , we know dummy never moved 

