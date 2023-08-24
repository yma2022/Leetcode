# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummyHead = ListNode()
        # dummyHead.next = head
        # curr = dummyHead
        # while curr.next and curr.next.next:
        #     dst = curr.next.next.next
        #     src = curr.next
        #     curr.next = curr.next.next
        #     curr.next.next = src
        #     src.next = dst
        #     curr = curr.next.next
        # return dummyHead.next
        if not head or not head.next:
            return head
        
        first_node = head
        second_node = head.next
        
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node
        
        return second_node
            
            
        