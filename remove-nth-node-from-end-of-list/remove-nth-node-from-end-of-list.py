# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head
        
        slow = dummyHead
        fast = dummyHead
        index = n
        
        while fast.next:
            if index > 0:
                index -= 1
                fast = fast.next
            else:
                fast = fast.next
                slow = slow.next
        # print(slow, fast)
        slow.next = slow.next.next
        return dummyHead.next
        