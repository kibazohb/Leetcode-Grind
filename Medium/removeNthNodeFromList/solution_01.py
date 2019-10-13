# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        behind = curr = head
        for i in range(n):
            curr = curr.next
        if curr is None:
            return head.next
        while curr.next != None:
            curr = curr.next
            behind = behind.next
            
        behind.next = behind.next.next
        
        
        return head
