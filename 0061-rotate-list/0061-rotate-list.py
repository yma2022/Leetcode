# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # find len
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
        if n <= 1:
            return head
        k = k % n
        if k == 0:
            return head
        
        slow, fast = head, head
        while fast.next:
            if k > 0:
                k -= 1
                fast = fast.next
            else:
                fast = fast.next
                slow = slow.next
        # print(slow, fast)
        dummy = ListNode()
        temp = slow.next
        dummy.next = temp
        slow.next = None
        fast.next = head
        return dummy.next
        