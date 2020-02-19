class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        answer = ListNode(0)
        ans = answer
        while l1 and l2:
            if l1.val + l2.val + carry <= 9:
                ans.next = ListNode(l1.val + l2.val + carry)
                ans = ans.next
                l1 = l1.next
                l2 = l2.next
                carry = 0
                
            else:
                ans.next = ListNode((l1.val + l2.val+ carry) % 10)
                ans = ans.next
                carry = (l1.val + l2.val + carry) // 10
                l1 = l1.next
                l2 = l2.next
        
        while l1:
            if l1.val + carry <= 9:
                ans.next = ListNode(l1.val + carry)
                ans = ans.next
                l1 = l1.next
                carry = 0
            else:
                ans.next = ListNode((l1.val + carry) % 10)
                ans = ans.next
                carry = (l1.val + carry)  // 10
                l1 = l1.next    
        while l2:
            if l2.val + carry <= 9:
                ans.next = ListNode(l2.val + carry)
                ans = ans.next
                l2 = l2.next
                carry = 0
            else:
                ans.next = ListNode((l2.val + carry)  % 10)
                ans = ans.next
                carry = (l2.val + carry)  // 10
                l2 = l2.next
        if carry:
            ans.next = ListNode(carry)
            ans = ans.next    
        return answer.next  
