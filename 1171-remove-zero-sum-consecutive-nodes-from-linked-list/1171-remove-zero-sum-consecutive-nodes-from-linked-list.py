# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        d = {0:dummy} # key is the prefix sum, value is the last node of getting this sum value, which is l5
        while head:
            prefix += head.val
            d[prefix] = head
            head = head.next
		# Go from the dummy node again to set the next node to be the last node for a prefix sum 
        head = dummy
        prefix = 0
        while head:
            prefix += head.val
            head.next = d[prefix].next
            head = head.next
        
        return dummy.next

        