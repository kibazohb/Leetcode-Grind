class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            temp_nxt = slow.next
            slow.next = node
            node = slow
            slow = temp_nxt
        # compare the first and second half nodes
        while node: # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
