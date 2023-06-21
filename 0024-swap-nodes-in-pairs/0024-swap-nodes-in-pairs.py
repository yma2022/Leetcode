# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head
        curr = dummyHead
        while curr and curr.next and curr.next.next:
            temp = curr.next # 防止节点修改
            temp1 = curr.next.next.next
            
            curr.next = curr.next.next
            curr.next.next = temp
            temp.next = temp1
            curr = curr.next.next
        return dummyHead.next
            
        