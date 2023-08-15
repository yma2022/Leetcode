# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def end_of_first_half(head):
            fast = head
            slow = head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        def reverse_list(head):
            prev = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        if not head:
            return True
        
        first_half_end = end_of_first_half(head)
        second_half_start = reverse_list(first_half_end.next)
        
        result = True
        first_pos = head
        second_pos = second_half_start
        
        while result and second_pos:
            if first_pos.val != second_pos.val:
                return False
            first_pos = first_pos.next
            second_pos = second_pos.next
            
        return result