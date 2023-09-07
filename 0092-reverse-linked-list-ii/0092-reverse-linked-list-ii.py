# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        index = 1
        dummyHead = ListNode()
        dummyHead.next = head
        prev = dummyHead

        reverse_start = dummyHead
        while reverse_start.next and index < left:
            reverse_start = reverse_start.next
            index += 1

        prev = reverse_start
        curr = prev.next
        while curr and index <= right:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            index += 1  
        reverse_start.next.next = curr 
        reverse_start.next = prev
        
        return dummyHead.next
                
        