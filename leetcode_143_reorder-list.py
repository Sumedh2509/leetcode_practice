'''
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

In the general case, label the nodes by their original zero-based positions from 0 to n - 1. After reordering, those original positions appear in this order:

[0, n-1, 1, n-2, 2, n-3, ...]

These numbers represent node positions, not the values stored in the nodes.

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.


Example 1:

Input: head = [2,4,6,8]

Output: [2,8,4,6]

Example 2:

Input: head = [2,4,6,8,10]

Output: [2,10,4,8,6]

Constraints:

1 <= Length of the list <= 1000.
1 <= Node.val <= 1000
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #idea/thoughts - the brute force way to do it would be to first store all the values in an array 
        #then just use two pointers and make a new list?


        array = []
        while head:
            array.append(head)
            head = head.next

        array2 = []
        l, r = 0 , len(array)-1
        while l<=r:
            array2.append(array[l])
            array2.append(array[r])
            l+=1
            r-=1

        for i in range(len(array2)-1):
            array2[i].next = array2[i+1]

        array2[-1].next = None
            




#imagine , making 2 linked lists , one half will contain the smoler values and the other bigger
#then we can reverse the links of the 2nd part, by using the method we used in reverse linked list problem
#to determine which is the 2nd half we can use slow and fast pointers

#as fast has twice the speed of slow
#when fast ends , slow will be at the middle
#that's how we determine where the 2nd half starts
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #determining the 2nd half
        slow, fast = head, head.next 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        #reversing the 2nd list

        second = slow.next #second is the first element of the 2nd half of list
        node = slow.next = None  #making node = none earlier as it is what we are iterating thru
        #slow.next = ?why?
        while second: #while second doesn't become none 
            tmp = second.next #temporarily storing, the next value as we are gonna reverse the link
            second.next = node #second.next now points to the previous element in 
            node = second #pushing the node to next step
            second = tmp  #pushing the second to next step


        #merging two lists

        first, second = head, node #setting up where we are going to iterate from 
        #node becomes the head of second linked list
        while second: 
            tmp1, tmp2 = first.next, second.next #since we are going to change where they will point, we store them temporarily
            first.next = second #setting what first points 2
            second.next = tmp1  #what our second points two 
            first, second = tmp1, tmp2 #then we increment the valuee
